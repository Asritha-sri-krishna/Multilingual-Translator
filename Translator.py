import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from googletrans import Translator, LANGUAGES
import pyttsx3
from PIL import Image, ImageTk
# Create Tkinter Window
root = tk.Tk()
root.title('Language Translator')
root.geometry('800x500')
root.minsize(800, 500)

# Configure rows and columns for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Initialize Translator and Text-to-Speech Engine
translator = Translator()
engine = pyttsx3.init()

# Language Code Mapping
language_codes = {name.capitalize(): code for code, name in LANGUAGES.items()}

# Function to dynamically resize the background image


root = tk.Tk()
root.title('Language Translator')
root.geometry('800x500')
root.minsize(800, 500)

# Set Background Color to Black
root.configure(bg="white")

# Configure rows and columns for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
# Function to translate text
def translate():
    language_1 = t1.get("1.0", "end-1c")
    cl = language_codes.get(choose_language.get(), None)

    if not language_1:
        messagebox.showerror('Language Translator', 'Please fill the input box')
    elif not cl:
        messagebox.showerror('Language Translator', 'Please select a valid language')
    else:
        t2.delete(1.0, 'end')
        try:
            output = translator.translate(language_1, dest=cl)
            t2.insert('end', output.text)
        except Exception as e:
            messagebox.showerror('Error', f"Translation failed: {e}")

# Function to clear input and output fields
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# Function to speak the translated text
from gtts import gTTS
import os

def speak():
    text_to_speak = t2.get("1.0", "end-1c")
    selected_language = language_codes.get(choose_language.get(), None)
    if text_to_speak:
        if selected_language:
            try:
                # Generate speech from text
                tts = gTTS(text=text_to_speak, lang=selected_language, slow=False)
                tts.save("output.mp3")  # Save the speech to an audio file

                # Play the audio file
                os.system("start output.mp3")  # Windows
                # For MacOS or Linux, use: os.system("afplay output.mp3") or os.system("mpg123 output.mp3")
            except Exception as e:
                messagebox.showerror('Error', f"Speech generation failed: {e}")
        else:
            messagebox.showerror('Language Translator', 'Please select a valid language for speech synthesis.')
    else:
        messagebox.showwarning('Language Translator', 'No text to speak')


# Function to translate and save text file
def convert_file():
    input_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not input_file_path:
        return

    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt")])

    if not output_file_path:
        return

    cl = language_codes.get(choose_language.get(), None)
    if not cl:
        messagebox.showerror('Language Translator', 'Please select a valid language')
        return

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        translated_content = translator.translate(content, dest=cl).text

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(translated_content)

        messagebox.showinfo("Success", f"Translated file saved as {output_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"File conversion failed: {e}")

# Language Dropdown (Right Side, Top Center)
language_selected = tk.StringVar()
choose_language = ttk.Combobox(root, width=20, textvariable=language_selected, state='readonly', font=('Verdana', 12, 'bold'))
choose_language['values'] = sorted(language_codes.keys())  # Sorted language names
choose_language.current(0)
choose_language.grid(row=0, column=1, pady=10, sticky='n')

# Labels for Default and Language Dropdowns
default_label = tk.Label(root, text="Default", font=("Verdana", 12, "bold"), bg="#FFE4E1")
default_label.grid(row=0, column=0, pady=10, sticky="n")
#language_label = tk.Label(root, text="Language", font=("Verdana", 12, "bold"), bg="#FFE4E1")
#language_label.grid(row=0, column=1, sticky="n")

# Input Text Box (Left Side)
t1 = tk.Text(root, wrap="word", bg="#FFFACD", fg="#000", borderwidth=5, relief=tk.RIDGE, height=10)
t1.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

# Output Text Box (Right Side)
t2 = tk.Text(root, wrap="word", bg="#D8BFD8", fg="#000", borderwidth=5, relief=tk.RIDGE, height=10)
t2.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

# Buttons directly aligned at the down middle


clear_button = tk.Button(root, text='Clear', bg="#32CD32", width=12, height=2, command=clear)
clear_button.grid(row=2, column=0, pady=10, padx=10,sticky="e")

translate_button = tk.Button(root, text='Translate', bg="#4682B4", width=12, height=2, command=translate)
translate_button.grid(row=2, column=0, pady=10, padx=10)

speak_button = tk.Button(root, text='Speak', bg="#FFD700", width=12, height=2, command=speak)
speak_button.grid(row=2, column=1, pady=10, padx=10,sticky="w")

convert_button = tk.Button(root, text='Convert File', bg="#FF4500", width=12, height=2, command=convert_file)
convert_button.grid(row=2, column=1, pady=10, padx=10)



# Run the application
root.mainloop()
