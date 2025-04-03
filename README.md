# 🎩 Band Baaja Bot - Your AI Wedding Assistant 💍

![Band Baaja Bot](thumbnail.png)

Band Baaja Bot is an AI-powered wedding assistant that helps you with wedding planning – from suggesting grand wedding menus to finding the best catering services. It is built using **SmolAgents**, **Gradio**, and **LiteLLM (Google Gemini API)**.

---

## 🚀 Features
- **Suggest Traditional Wedding Menus** (Gujarati, Bengali, Punjabi, etc.)
- **Find the Best Catering Services**
- **Search for Wedding Trends** using DuckDuckGo
- **Visit Webpages for Additional Research**

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Band_Baaja_Bot.git
cd Band_Baaja_Bot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set API Keys (For Local Testing)
Create a `.env` file in the root directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_google_gemini_api_key
```
Then, load the `.env` file in your `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

### 4️⃣ Run the App
```bash
python app.py
```
The application will start and be accessible at:
```
http://0.0.0.0:7860
```

---

## 🖥️ How to Use
1. Open the web interface after running the app.
2. Enter your wedding-related query (e.g., *"Suggest me a grand Gujarati wedding menu"*).
3. Receive AI-powered responses instantly!

---

## 🎯 Future Enhancements
- Multi-language Support
- Integration with Wedding Vendors
- AI-powered Budget Planning

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues for any feature suggestions or bug fixes.

---

## 📝 License
This project is licensed under the **Apache 2.0 License**.

---

## 🌐 Try it on Hugging Face Spaces
You can also run this bot on Hugging Face Spaces:  
➡️ [Band Baaja Bot on Hugging Face](https://huggingface.co/spaces/21spl/Band_Baaja_Bot)

---
💖 Developed with Love for Indian Weddings! 🇮🇳



