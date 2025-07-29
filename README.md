# Myanmar-Food-Quiz-with-Image
This is a Streamlit web app that uses Google Gemini (Multimodal) to answer multiple choice questions (MCQs) based on an uploaded image of a Myanmar food dish.
It combines image understanding with natural language to evaluate answers and measure model performance.
To show the model predictions and accuracy according to myanmar food images+MCQs.

## 🚀 Features

1. Upload any image of a Myanmar traditional food (e.g., မုန့်ဟင်းခါး, မုန့်လင်မယား)

2. Paste multiple-choice questions in Burmese

3. Automatically sends image + question to Gemini Vision model

4. Displays Gemini's answer vs. the correct one

5. Provides performance evaluation with:

6. ✔️ Accuracy Score

7. 📊 Classification Report

## 🛠️ Technologies Used

-Streamlit

-Google Generative AI (Gemini)

-Pillow (PIL)

-scikit-learn


## 📦 Installation

Clone the repo:
```bash
git clone https://github.com/yourusername/myanmar-food-quiz.git
cd myanmar-food-quiz
```
Install dependencies:
```bash
pip install -r requirements.txt
```

## 📋 Question Format
```bash
Paste your questions in the following format (in Burmese):

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
### Select one image and type your questions with answers.
<img width="1886" height="657" alt="Image" src="https://github.com/user-attachments/assets/42bb191a-e4dd-4e06-ae0e-7fd86b7d69b0" />

### Website shows your used image.
<img width="665" height="436" alt="Image" src="https://github.com/user-attachments/assets/52b3c632-4244-493c-b3fc-73c7f8698035" />

### Gemini Fully Response
<img width="1334" height="545" alt="Image" src="https://github.com/user-attachments/assets/4aa6f524-87f7-4b82-8193-bcda330a0acd" />

### Model accuracy
<img width="1362" height="516" alt="Image" src="https://github.com/user-attachments/assets/464d169c-05cc-4aba-9656-affe01d9f8cc" />
