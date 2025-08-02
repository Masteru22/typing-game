import tkinter as tk
from tkinter import *
from words import add_sentence
from logic import verify_if_correct, remove_first_word
from ui import display_colored_sentence

WIDTH, HEIGHT = 800, 500
GAME_DURATION = 60
sentence = ""
CPM = 0
WPM = 0

def game_start():
    global sentence, CPM, WPM
    start_label.pack_forget()
    start_button.pack_forget()
    restart_button.pack_forget()
    result_label.pack_forget()

    CPM = 0
    WPM = 0
    CPM_COUNT_label.config(text=CPM)
    WPM_COUNT_label.config(text=WPM)

    sentence = add_sentence()
    display_colored_sentence(text_label, sentence)
    count_down(GAME_DURATION)

    CPM_label.pack(side="left", padx=2)
    CPM_COUNT_label.pack(side="left", padx=(0, 12))
    WPM_label.pack(side="left", padx=2)
    WPM_COUNT_label.pack(side="left", padx=(0, 12))
    SECONDS_label.pack(side="left", padx=2)
    SECONDS_COUNT_label.pack(side="left", padx=(0, 12))

    text_label.pack(pady=(60, 10))
    writing_entry.delete(0, END)
    writing_entry.pack()
    writing_entry.focus_set()

def game_stop():
    text_label.pack_forget()
    writing_entry.pack_forget()
    CPM_label.pack_forget()
    CPM_COUNT_label.pack_forget()
    WPM_label.pack_forget()
    WPM_COUNT_label.pack_forget()
    SECONDS_label.pack_forget()
    SECONDS_COUNT_label.pack_forget()

    result_label.config(text=f"WELL DONE! YOUR SCORE IS:\nCPM: {CPM} WPM: {WPM}", font=("Helvetica", 15), bg="#f0f0f0")
    result_label.pack()
    restart_button.pack()

def count_down(count):
    SECONDS_COUNT_label.config(text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        game_stop()

def space(event):
    global sentence, CPM, WPM
    word = writing_entry.get()
    writing_entry.delete(0, END)
    if verify_if_correct(word, sentence):
        CPM += len(word) - 1
        WPM += 1
        CPM_COUNT_label.config(text=CPM)
        WPM_COUNT_label.config(text=WPM)
    sentence = remove_first_word(sentence, add_sentence)
    display_colored_sentence(text_label, sentence)

# GUI setup
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.configure(bg="#f0f0f0")

frame = Frame(window, bg="#f0f0f0")
frame.pack()

start_label = Label(window, text="Welcome to my typing speed program", font=("Helvetica", 24), bg="#f0f0f0")
start_label.pack()
start_button = Button(window, text="START", command=game_start, font="24")
start_button.pack(pady=100)

writing_entry = Entry(window, width=30, font=("Helvetica", 24), justify='center')
text_label = tk.Text(window, width=40, height=2, font=("Helvetica", 24), bd=0, highlightthickness=0, bg="#f0f0f0")
text_label.configure(state="disabled")

display_colored_sentence(text_label, add_sentence())

CPM_label = Label(frame, text="CPM:", font=("Helvetica", 15), bg="#f0f0f0")
CPM_COUNT_label = Label(frame, text=CPM, font=("Helvetica", 15), bg="#f0f0f0")
WPM_label = Label(frame, text="WPM:", font=("Helvetica", 15), bg="#f0f0f0")
WPM_COUNT_label = Label(frame, text=WPM, font=("Helvetica", 15), bg="#f0f0f0")
SECONDS_label = Label(frame, text="SECONDS:", font=("Helvetica", 15), bg="#f0f0f0")
SECONDS_COUNT_label = Label(frame, text="0", font=("Helvetica", 15), bg="#f0f0f0")

result_label = Label(frame, text="", bg="#f0f0f0")
restart_button = Button(window, text="RESTART", command=game_start, font="24")

window.bind('<space>', space)
window.mainloop()
