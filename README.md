# 🤖 J.A.R.V.I.S-AI

An AI-based voice assistant that listens to your commands and performs actions like opening websites, logging into Instagram, and telling the current time — just like J.A.R.V.I.S from Iron Man!

---

## 🎙️ Voice Assistant using Python

This is a simple voice-controlled assistant built in Python that:
- Listens to your voice commands
- Opens commonly used websites
- Logs you into Instagram using Selenium
- Speaks responses out loud
- Tells the current system time

---

## 🔧 Features

- 🎤 Speech recognition via microphone using `speech_recognition`
- 🗣️ Voice responses using Windows' speech API (`win32com`)
- 🌐 Opens websites like YouTube, Google, Facebook, etc.
- 📸 Automates Instagram login via Selenium
- ⏰ Tells the system time when asked

---

## 🧠 Technologies Used

- Python 3
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/)
- [`pypiwin32`](https://pypi.org/project/pypiwin32/) for text-to-speech
- [`selenium`](https://pypi.org/project/selenium/)
- `webbrowser` module
- `datetime` module
- Microsoft Edge + Edge WebDriver

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Vansh111000/J.A.R.V.I.S-AI.git
cd J.A.R.V.I.S-AI
```
### 2. Install Required Packages
```bash
pip install SpeechRecognition
pip install pypiwin32
pip install selenium
pip install openai
```
### 3. Configure Edge WebDriver
Make sure Microsoft Edge and the Edge WebDriver are installed on your system. Update the path to the WebDriver in the script:

python
```bash
driver_path = "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"
```
### 4. Update Instagram Credentials
Replace the placeholders in the script with your actual Instagram username and password:

python
```bash
username_input.send_keys("YOUR_USERNAME")
password_input.send_keys("YOUR_PASSWORD")
```
### 5. Run the Assistant
```bash

python your_script_name.py
```
---
## 🗣️ Example Voice Commands
- Open YouTube

- Open Google

- Open Facebook

- Open Instagram (performs auto login)

- Open time (tells the current time)
 
---

## 🛑 Known Limitations
- ⚠️ Only works on Windows (uses win32com.client)

- 🌐 Requires an internet connection for speech recognition and website access

- 🔐 Credentials are hardcoded (insecure for production)
  
---
## 📌 To-Do
 - Add GUI interface

 - Use .env for credentials

 - Add more commands

 - Make OS-independent
---
## 🤝 Contributing
Pull requests and suggestions are welcome!
Feel free to fork this repo and enhance it.

---

## 📄 License
This project is open-source and available under the MIT License.

---
## 👋 Acknowledgments
- OpenAI

- SpeechRecognition Library

- Selenium

- Microsoft SAPI (Speech API)
