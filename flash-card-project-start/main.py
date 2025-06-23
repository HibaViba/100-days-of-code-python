import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    df = pandas.read_csv("../flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("../flash-card-project-start/data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash card ")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
card_front_img = PhotoImage(file="../flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="../flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 30, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="../flash-card-project-start/images/right.png")
button_right = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
button_right.grid(column=0, row=1)

wrong_img = PhotoImage(file="../flash-card-project-start/images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(column=1, row=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
