# Myanmar-Food-Quiz-with-Gemini
This is a Streamlit web app that uses Google Gemini (Multimodal) to answer multiple choice questions (MCQs) based on an uploaded image of a Myanmar food dish.
It combines image understanding with natural language to evaluate answers and measure model performance.
To show the model predictions and accurancy according to myanmar food images+MCQs.

## 🚀 Features
```bash
    Upload any image of a Myanmar traditional food (e.g., မုန့်ဟင်းခါး, မုန့်လင်မယား)

    Paste multiple-choice questions in Burmese

    Automatically sends image + question to Gemini Vision model

    Displays Gemini's answer vs. the correct one

    Provides performance evaluation with:

        ✔️ Accuracy Score

        📊 Classification Report
```
## 🛠️ Technologies Used
```bash
    Streamlit

    Google Generative AI (Gemini)

    Pillow (PIL)

    scikit-learn
```

## 📦 Installation
```bash
    Clone the repo:

git clone https://github.com/yourusername/myanmar-food-quiz.git
cd myanmar-food-quiz

Install dependencies:

pip install -r requirements.txt
```

## 📋 Question Format
```bash
Paste your questions in the following format (in Burmese or English):

Q1: မုန့်ဟင်းခါးရဲ့အဓိကအသားကဘာလဲ?
A. ကြက်သား
B. ငါး
C. ဝက်သား
D. ဆိတ်သား
Answer: B

Q2: မုန့်ဟင်းခါးကို ဘယ်အချိန်စားလေ့ရှိသလဲ?
A. နံနက်စာ
B. နေ့လယ်စာ
C. ညစာ
D. ညနေစာ
Answer: A
```

<img width="1886" height="657" alt="Image" src="https://github.com/user-attachments/assets/42bb191a-e4dd-4e06-ae0e-7fd86b7d69b0" />

<img width="665" height="436" alt="Image" src="https://github.com/user-attachments/assets/52b3c632-4244-493c-b3fc-73c7f8698035" />

<img width="1334" height="545" alt="Image" src="https://github.com/user-attachments/assets/4aa6f524-87f7-4b82-8193-bcda330a0acd" />

<img width="1362" height="516" alt="Image" src="https://github.com/user-attachments/assets/464d169c-05cc-4aba-9656-affe01d9f8cc" />
