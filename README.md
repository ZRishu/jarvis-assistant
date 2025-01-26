# Jarvis Assistant

Jarvis Assistant is a Python-based voice assistant that can perform various tasks like sending emails, searching the web, providing news updates, generating passwords, and more. It uses speech recognition and text-to-speech functionalities to interact with users.

## Features

- *Voice Interaction:* Recognizes voice commands using speech_recognition.
- *Text-to-Speech:* Converts text to speech using pyttsx3.
- *Email Sending:* Sends emails using SMTP.
- *Google Search & Wikipedia:* Retrieves search results and Wikipedia summaries.
- *WhatsApp Messaging:* Sends messages via WhatsApp Web.
- *News Updates:* Fetches top headlines using NewsApiClient.
- *Jokes & Fun:* Tells jokes, flips a coin, and rolls a die.
- *File Operations:* Can open files and remember notes.
- *Password Generator:* Creates random secure passwords.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fierce-adventurer/jarvis-assistant.git
   cd jarvis-assistant
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Set up your secrets_1.py file:
   ```python
   senderemail = 'xyz@gmail.com'
   epwd = 'abc@1234'
   to = 'anyone@gmail.com'
   
4. Run the assistant:
   ```bash
   python jarvis.py
   

## Usage

- Start the assistant and use voice commands such as:
  - "Jarvis, what is the time?"
  - "Send an email"
  - "Search Google for Python tutorials"
  - "Tell me a joke"
  - "Generate a password"

## Requirements

- Python 3.x
- Required libraries:
  ```bash
  pip install pyttsx3 speechrecognition smtplib pyautogui wikipedia pywhatkit newsapi clipboard nltk pyjokes
  

## Contributing

Feel free to fork the project and submit pull requests!

## License

This project is licensed under the MIT License.
