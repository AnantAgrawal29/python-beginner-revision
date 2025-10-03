BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random, pandas

to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

random_word = random.choice(to_learn)


# remove words
def remove_word():
    global flip_timer
    try:
        to_learn.remove(random_word)
        create_card()
    except IndexError:
        print("all done")
        window.after_cancel(flip_timer)


# Flip Cards
def flip_card(random_word):
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")


# Creating New Flash Cards
def create_card():
    global flip_timer, random_word, random_index
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    flip_timer = window.after(3000, flip_card, random_word)


# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
btn_wrong = PhotoImage(file="images/wrong.png")
btn_right = PhotoImage(file="images/right.png")

flip_timer = window.after(3000, flip_card, random_word)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 264, image=card_front)
language = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(
    400, 263, text=random_word["French"], font=("Arial", 60, "bold")
)
canvas.grid(column=0, row=0, columnspan=3)

wrong = Button(
    image=btn_wrong,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    command=create_card,
)
wrong.grid(column=0, row=1)
right = Button(
    image=btn_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_word
)
right.grid(column=2, row=1)
window.mainloop()

pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
