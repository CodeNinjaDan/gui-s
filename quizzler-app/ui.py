from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.create_widgets()
        self.get_next_question()
        self.window.mainloop()


    def create_widgets(self):
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Question", font=("Arial", 20, "italic"),
                                        fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="/home/dan/PycharmProjects/gui-s/quizzler-app/images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_img = PhotoImage(file="/home/dan/PycharmProjects/gui-s/quizzler-app/images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)