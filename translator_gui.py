import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize Translator
translator = Translator()

# Function to perform translation
def translate_text():
    input_text = input_text_box.get("1.0", tk.END).strip()
    target_language_code = target_language_combobox.get()

    if not input_text:
        messagebox.showerror("Error", "Please enter text to translate!")
        return

    if not target_language_code:
        messagebox.showerror("Error", "Please select a target language!")
        return

    try:
        translation = translator.translate(input_text, dest=target_language_code)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

# Function to populate language combobox
def populate_languages():
    return {code: lang.title() for code, lang in LANGUAGES.items()}

# Create GUI window
app = tk.Tk()
app.title("Language Translation Tool")
app.geometry("500x400")

# Input Text
tk.Label(app, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
input_text_box = tk.Text(app, height=5, wrap="word", font=("Arial", 10))
input_text_box.pack(padx=10, pady=5, fill="x")

# Target Language
tk.Label(app, text="Select Target Language:", font=("Arial", 12)).pack(pady=5)
languages = populate_languages()
language_list = list(languages.values())
language_codes = list(languages.keys())

target_language_combobox = ttk.Combobox(app, values=language_list, state="readonly", font=("Arial", 10))
target_language_combobox.pack(padx=10, pady=5, fill="x")

# Translate Button
translate_button = tk.Button(app, text="Translate", command=translate_text, font=("Arial", 12), bg="blue", fg="white")
translate_button.pack(pady=10)

# Output Text
tk.Label(app, text="Translated Text:", font=("Arial", 12)).pack(pady=5)
output_text_box = tk.Text(app, height=5, wrap="word", font=("Arial", 10), state="normal")
output_text_box.pack(padx=10, pady=5, fill="x")

# Run the application
app.mainloop()
