import streamlit as st
import google.generativeai as genai
from PIL import Image
import re
import io
from sklearn.metrics import classification_report, accuracy_score

# ======= Gemini Config =======
# Make sure to replace "YOUR_API_KEY" with your actual Gemini API key.
# It is recommended to use st.secrets for key management in a deployed app.
genai.configure(api_key="AIzaSyD23K5kQpeCidAj_HW4vnSVtrOZKltnPkI") 
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Myanmar Food Quiz", layout="wide")

# ======= Sidebar =======
st.sidebar.title("📋 Menu")
submit_button = st.sidebar.button("🚀 Submit Questions")
st.sidebar.markdown("Made for Myanmar food image Q&A using Gemini Vision.")

# ======= Main UI =======
st.title("🍜 မြန်မာဟင်းလျာ Q&A (Multiple Choice with Gemini)")

uploaded_file = st.file_uploader("📷 မုန့်/ဟင်းလျာ ပုံတင်ပါ", type=["jpg", "jpeg", "png"])

question_input = st.text_area(
    "📝 မေးခွန်းများကို Paste လုပ်ပါ (မြန်မာဘာသာဖြင့်)",
    placeholder="Q1: မေးခွန်း\nA. ရွေး ၁\nB. ရွေး ၂\nC. ရွေး ၃\nD. ရွေး ၄\nAnswer: B\n\nQ2:...",
    height=300
)

# ======= Helper Functions =======

def parse_mcqs_with_answers(text):
    """Parses the multiline string of MCQs into a list of question dictionaries."""
    questions = []
    # Use a more robust regex to split questions, handling various spacings
    blocks = re.split(r'\n*(Q\d+[:.])', text.strip())
    if not blocks[0]: # If the text starts with Q1, the first element will be empty
        blocks = blocks[1:]

    combined = []
    for i in range(0, len(blocks), 2):
        if i + 1 < len(blocks):
            combined.append(blocks[i] + blocks[i + 1])

    for block in combined:
        lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
        if len(lines) >= 6:
            q_line = lines[0]
            choices = lines[1:5]
            answer_line = lines[5]

            question_text = re.sub(r'^Q\d+[:.]\s*', '', q_line).strip()
            answer_match = re.search(r'Answer\s*[:\-]?\s*([ABCD])', answer_line, re.IGNORECASE)

            if answer_match:
                correct = answer_match.group(1).upper()
                questions.append({
                    "question": question_text,
                    "choices": choices,
                    "answer": correct
                })
    return questions

def extract_answer(text):
    """Extracts the first single letter A, B, C, or D from the model's response."""
    # Look for a letter that is a standalone word
    match = re.search(r'\b([ABCD])\b', text.strip().upper())
    return match.group(1) if match else "?"

# ======= Submit Button Logic =======
if submit_button:
    if not uploaded_file or not question_input:
        st.warning("📷 ပုံနှင့် 📝 မေးခွန်းများနှစ်ခုစလုံးလိုအပ်ပါသည်။")
    else:
        try:
            image = Image.open(uploaded_file)

            # Display the uploaded image
            st.image(image, caption="📷 အသုံးပြုမည့်ပုံ", width=400)

            mcq_list = parse_mcqs_with_answers(question_input)
            if not mcq_list:
                st.error("မေးခွန်းများကို 'Q1:', 'A.', 'B.', 'C.', 'D.', 'Answer: A' ပုံစံအတိုင်းရေးပါ။")
            else:
                st.subheader("📊 Gemini ရဲ့ ဖြေချက်များ")
                true_answers = []
                predicted_answers = []

                # --- The main loop for processing each question ---
                for i, q in enumerate(mcq_list, 1):
                    prompt = f"""
ပုံကိုကြည့်ပြီး အောက်ပါ multiple choice မေးခွန်းကို ဖြေပါ။

မေးခွန်း: {q['question']}

ရွေးချယ်စရာများ:
{q['choices'][0]}
{q['choices'][1]}
{q['choices'][2]}
{q['choices'][3]}

အဖြေမှန်၏ အက္ခရာ (A, B, C, or D) တစ်လုံးတည်းကိုသာ ပြန်လည်ဖြေကြားပေးပါ။
"""

                    with st.spinner(f"🤖 Gemini ကို မေးနေသည် (Q{i})..."):
                        try:
                            # ***FIXED CODE HERE***
                            # Pass the prompt and the PIL Image object directly in a list.
                            # The library handles the conversion.
                            response = model.generate_content([prompt, image])
                            
                            response_text = response.text.strip()
                            gemini_answer = extract_answer(response_text)
                        
                        except Exception as e:
                            gemini_answer = "?"
                            # Make the error message more user-friendly
                            response_text = f"An error occurred while contacting the Gemini API: {e}"
                            st.error(f"Error processing Question {i}: {e}")

                    true_answers.append(q["answer"])
                    predicted_answers.append(gemini_answer)

                    # Display results for each question
                    st.markdown(f"--- \n#### ❓ မေးခွန်း {i}: {q['question']}")
                    for choice in q['choices']:
                        # Highlight correct and predicted answers for clarity
                        label = ""
                        if q['answer'] in choice:
                            label += " ✔️ (မှန်)"
                        if gemini_answer in choice and q['answer'] != gemini_answer:
                            label += " 🤖 (Gemini)"
                        elif gemini_answer in choice and q['answer'] == gemini_answer:
                             label += " 🤖 (Gemini မှန်)"
                        st.write(f"{choice}{label}")

                    st.markdown(f"**✔️ မှန်ကန်သောအဖြေ**: `{q['answer']}`")
                    st.markdown(f"**🤖 Gemini ဖြေသည်**: `{gemini_answer}`")

                    # Use an expander for the full, raw response
                    with st.expander("🧾 Gemini Full Response ကြည့်ရန်"):
                        st.code(response_text, language=None)

                # ======= Evaluation =======
                st.subheader("📈 စုစုပေါင်းအဖြေစစ်ခြင်း")
                if len(true_answers) > 0:
                    correct_count = sum(1 for a, b in zip(true_answers, predicted_answers) if a == b)
                    accuracy = accuracy_score(true_answers, predicted_answers)
                    st.success(f"✅ **မှန်ကန်သောအဖြေ**: {correct_count} / {len(true_answers)}")
                    st.info(f"🎯 **Accuracy**: {accuracy:.2%}")

                    # Generate and display the classification report
                    report = classification_report(
                        true_answers, 
                        predicted_answers, 
                        labels=['A', 'B', 'C', 'D'], # Ensure all labels are present
                        output_dict=True, 
                        zero_division=0
                    )
                    st.dataframe(report)
        
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")