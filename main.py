from tkinter import *
import time
from tkinter import ttk
from faker import Faker
from ttkbootstrap.constants import *
from tkinter import messagebox

window = Tk()
window.title("typing-speed: watch out wrong words not counted")
window.geometry("900x600")
window.config(bg="green")

new_text_tolist = None

count_for_question_mark = 0
count_for_comma = 0
typing_words = " "
fake = Faker()
compare_word = []
timer = None
counter = None

original_words = [fake.word() for _ in range(40)]
for word in original_words:
    count_for_comma += 1
    count_for_question_mark += 1
    compare_word.append(word)
    typing_words += word
    typing_words += " "

print(original_words)
print(compare_word)


def start_timer():
    create_timer(20)


def get_text(event):
    global counter
    counter = 0
    global new_text_tolist
    new_text = (bottom_inputtxt.get("1.0", END + "-1c") + event.char)
    new_text_tolist = new_text.split()

    for word_position in range(len(new_text_tolist)):
        if new_text_tolist[word_position] == compare_word[word_position]:
            counter += 1
            counter_label.config(text=f"Word Count: {counter}")
        elif new_text_tolist[word_position] not in compare_word[word_position]:
            counter += 0
            counter_label.config(text=f"Word Count: {counter}")


def create_timer(count):
    timer_label.config(text=f"Timer: {count}")

    if count > 0:
        global timer
        timer = window.after(1000, create_timer, count - 1)
        start_button.config(state="disabled")
    else:
        timer_label.config(text=f"Timer: 00")
        start_button.config(state="normal")
        messagebox.showinfo(title="Time up", message=f"Time up, you typed {counter} word(s) in 60 seconds")


def reset_timer():
    window.after_cancel(timer)
    # canvas.itemconfig(timer_text, text="00:00")
    # title_label.config(text="Timer")
    # check_marks.config(text="")
    # global reps
    # reps = 0


top_frame1 = Frame(window, width=800, height=30)
top_frame1.pack(pady=(10, 1))
timer_label = Label(top_frame1, text=" Timer: 00 ", fg="red", font=("Helvetica", 10))
timer_label.place(relx=1, x=-2, y=2, anchor=NE)
#


counter_label = Label(top_frame1, text=" Word Count: 00 ", fg="red", font=("Helvetica", 10))
counter_label.place(anchor=NW)

top_frame = Frame(window, width=800, height=300)
top_frame.pack(pady=(0, 20))

top_inputtxt = Text(top_frame, height=15, width=99, bg="light yellow")
top_inputtxt.insert(END, typing_words)
top_inputtxt.pack()

start_button = Button(text="Type to below", command=start_timer)
start_button.pack()
bottom_frame = Frame(window, width=800, height=200)
bottom_frame.pack()

bottom_inputtxt = Text(bottom_frame, height=10, width=99, bg="light yellow")
bottom_inputtxt.pack()
bottom_inputtxt.bind("<Key>", get_text)


window.mainloop()
