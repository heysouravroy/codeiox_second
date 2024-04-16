import tkinter as tk
from tkinter import filedialog

def count_words(file_name):
    word_count = {}
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?').lower()
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
    except UnicodeDecodeError:
        with open(file_name, 'r', encoding='latin-1') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?').lower()
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def analyze_file():
    file_name = entry_file_path.get()
    try:
        word_count = count_words(file_name)
        output_text.delete(1.0, tk.END)
        for word, count in word_count.items():
            output_text.insert(tk.END, f"{word}: {count}\n")
    except FileNotFoundError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: File '{file_name}' not found.")

root = tk.Tk()
root.title("Word Count Tool")

label_file_path = tk.Label(root, text="File Path:")
entry_file_path = tk.Entry(root, width=50)
button_browse = tk.Button(root, text="Browse", command=browse_file)
button_analyze = tk.Button(root, text="Analyze", command=analyze_file)
output_text = tk.Text(root, height=20, width=50)

label_file_path.grid(row=0, column=0, padx=5, pady=5)
entry_file_path.grid(row=0, column=1, padx=5, pady=5)
button_browse.grid(row=0, column=2, padx=5, pady=5)
button_analyze.grid(row=1, columnspan=3, padx=5, pady=5)
output_text.grid(row=2, columnspan=3, padx=5, pady=5)

root.mainloop()
