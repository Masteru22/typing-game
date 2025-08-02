import tkinter as tk

def display_colored_sentence(text_label, sentence):
    text_label.configure(state="normal")
    text_label.delete("1.0", tk.END)
    words = sentence.split()
    text_label.tag_configure("center", justify='center')

    for i, word in enumerate(words):
        if i == 0:
            text_label.insert(tk.END, word + " ", ("green", "center"))
        else:
            text_label.insert(tk.END, word + " ", ("black", "center"))

    text_label.tag_config("green", foreground="green")
    text_label.tag_config("black", foreground="black")
    text_label.configure(state="disabled")
