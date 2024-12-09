# Multilingual-Translator

A robust desktop application for translating text, generating speech, and converting text files into multiple languages. Built with Python, Tkinter, and Google Translate API, this project combines intuitive design and powerful features.

---

## **Features**
- **Text Translation**: Translate input text into multiple languages using the Google Translator module.
- **Speech Synthesis**: Convert translated text to speech and play it using the `gTTS` library.
- **File Conversion**: Translate text files into another language and save the translated content.
- **Dynamic Language Selection**: Over 100 supported languages with an easy-to-use dropdown menu.
- **User-Friendly Interface**: Responsive UI built with Tkinter, featuring clear input and output fields.

---

## **Technologies Used**
- **Programming Language**: Python  
- **Libraries**:
  - `Tkinter`: For the graphical user interface.
  - `Googletrans`: For language translation.
  - `gTTS`: For speech synthesis.
  - `Pillow`: For handling images (optional for advanced UI).
  - `Pyttsx3`: For offline text-to-speech synthesis (fallback).
- **File Handling**: `filedialog` for importing and exporting text files.

---

## **How to Run the Project**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/LanguageTranslator.git
   cd LanguageTranslator
   ```

2. **Install Required Libraries**:
   Ensure you have Python installed (preferably 3.8+). Then, install the required libraries:
   ```bash
   pip install googletrans==4.0.0-rc1 gtts pyttsx3 pillow
   ```

3. **Run the Application**:
   Execute the main script:
   ```bash
   python translator.py
   ```

---

## **How to Use**
1. **Text Translation**:
   - Enter text into the left input box.
   - Select the target language from the dropdown menu.
   - Click **Translate** to view the translated text in the right box.

2. **Speech Synthesis**:
   - Click **Speak** to hear the translated text.

3. **File Conversion**:
   - Click **Convert File** to select a text file for translation.
   - Choose the output file path and save the translated content.

4. **Clear Fields**:
   - Click **Clear** to reset input and output fields.

---

## **Screenshots**
### **Main Interface**
![Main Interface](https://github.com/Asritha-sri-krishna/Multilingual-Translator/blob/main/Language.png?raw=true)

---



## **Acknowledgments**
- Google Translator for powering the translations.
- Tkinter for providing a flexible GUI framework.
- OpenAI for assistance with project documentation.

---

