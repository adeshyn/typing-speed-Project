from tkinter import *
import time
from tkinter import ttk
from faker import Faker
from ttkbootstrap.constants import *
from tkinter import messagebox

window = Tk()
window.title("typing-speed: watch out wrong words are not counted")
window.geometry("900x600")
window.config(bg="#004225")

new_text_tolist = None

count_for_question_mark = 0
count_for_comma = 0
typing_words = " "
fake = Faker()
original_words = []
timer = None
counter = 0
new_count = []

original_words = [fake.word() for _ in range(40)]
for word in original_words:
    # count_for_comma += 1
    # count_for_question_mark += 1
    # compare_word.append(word)
    typing_words += word
    typing_words += " "

print(original_words)




def start_timer():
    nunu=00
    if top_inputtxt.get("1.0", END + "-1c"):
        create_timer(20)


    else:

        top_inputtxt.insert(END, typing_words)
        create_timer(20)
        word_count_label.config(text=f"Word Count: {nunu}")



def get_text(event, ):
    global counter
    counter = 0
    global new_text_tolist
    new_text = (bottom_inputtxt.get("1.0", END + "-1c") + event.char)
    new_text_tolist = new_text.split()

    for word_position in range(len(new_text_tolist)):
        if new_text_tolist[word_position] == original_words[word_position]:
            counter += 1
            word_count_label.config(text=f"Word Count: {counter}")
        elif new_text_tolist[word_position] not in original_words[word_position]:
            counter += 0
            word_count_label.config(text=f"Word Count: {counter}")


def create_timer(count):
    timer_label.config(text=f"Timer: {count}")
    global new_count
    time_used = 60 - count

    if count > 0:
        time_used += 1
        global timer
        timer = window.after(1000, create_timer, count - 1)
        start_button.config(state="disabled")

    else:
        timer_label.config(text=f"Timer: 00")
        word_count_label.config(text=f"Word Count: 00")
        start_button.config(state="normal")
        messagebox.showinfo(title="Time up", message=f"Time up, you typed {counter} word(s) in 60 seconds")


def clears():
    top_inputtxt.delete("1.0", "end")
    original_words.clear()

def reset_timer():
    window.after_cancel(timer)
    start_button.config(state="active")
    clears()
    bottom_inputtxt.delete("1.0", "end")
    messagebox.showinfo(title="Incomplete", message=f" Incomplete! {counter} word(s) typed so far\n Press OK and then start to try again")




frame_for_top_labels = Frame(window, width=800, height=30)
frame_for_top_labels.pack(pady=(10, 1))
timer_label = Label(frame_for_top_labels, text=" Timer: 00 ", fg="#FE0000", font=('Helvetica', 10,))
timer_label.place(relx=1, x=-2, y=2, anchor=NE)

word_count_label = Label(frame_for_top_labels, text=" Word Count: 00 ", fg="#FE0000", font=('Helvetica', 10))
word_count_label.place(anchor=NW)

frame_for_projected_words = Frame(window, width=800, height=300)
frame_for_projected_words.pack(pady=(0, 20))

top_inputtxt = Text(frame_for_projected_words, height=15, width=99, bg="#EBE4D1")
top_inputtxt.insert(END, typing_words)
top_inputtxt.pack()

frame_for_start_stop_labels = Frame(window, width=800, height=30)
frame_for_start_stop_labels.pack(pady=(10, 1))

start_button = Button(frame_for_start_stop_labels, text="Start", command=start_timer)
start_button.pack(side="left")

stop_button = Button(frame_for_start_stop_labels, text="Stop/Reset", command=reset_timer)
stop_button.pack(side="right")

bottom_frame = Frame(window, width=800, height=200)
bottom_frame.pack()

bottom_inputtxt = Text(bottom_frame, height=10, width=99, bg="#EBE4D1")
bottom_inputtxt.pack()
bottom_inputtxt.bind("<Key>", get_text)

window.mainloop()
