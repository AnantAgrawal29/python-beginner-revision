import time

from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.cancel = ""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0")
        self.score.config(bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300,height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280,text="", fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2 , pady=50)

        self.tick = PhotoImage(file="images/true.png")
        self.correct = Button(image=self.tick, highlightthickness=0, bg=THEME_COLOR, command=self.correct_ans)
        self.correct.grid(column=0, row=2, padx=(0, 10))

        self.cross = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.cross, highlightthickness=0, bg=THEME_COLOR, command=self.wrong_ans)
        self.wrong.grid(column=1, row=2, padx=(10, 0))

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
        if q_text == "Quiz Completed":
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def answer(self, ans: str):
        if self.quiz.check_answer(user_answer=ans):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.cancel = self.window.after(1000, func=self.get_next_question)
        self.score.config(text=f"Score: {self.quiz.score}")

    def correct_ans(self):
        self.answer('true')

    def wrong_ans(self):
        self.answer('false')
