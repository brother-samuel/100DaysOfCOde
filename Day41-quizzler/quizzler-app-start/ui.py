THEME_COLOR = "#375362"
import tkinter as tk
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
            self.quiz = quiz_brain

            self.root = tk.Tk()
            self.root.title("Quizzler")
            self.root.config(bg=THEME_COLOR,  padx=20,  pady=20)

            self.score_label = tk.Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
            self.score_label.grid(row=0, column=1)

            self.canvas = tk.Canvas(width=300, height=250, bg="white")
            self.question_text = self.canvas.create_text(150, 122, text="Here goes the question", width=275, fill="black", font=("Arial", 20, "italic"))
            self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

            tick_img = tk.PhotoImage(file="Day41-quizzler/quizzler-app-start/images/true.png")
            self.tick = tk.Button(image=tick_img, highlightthickness=0, command=self.check_if_true)
            self.tick.grid(row=2, column=0)

            cross_img = tk.PhotoImage(file="Day41-quizzler/quizzler-app-start/images/false.png")
            self.cross = tk.Button(image=cross_img, highlightthickness=0, command=self.check_if_false)
            self.cross.grid(row=2, column=1)

            self.get_next_question()

            self.root.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions.")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")


    def check_if_true(self):
         self.quiz.check_answer("True")
         self.get_next_question()   
        
    def check_if_false(self):
         self.quiz.check_answer("False")
         self.get_next_question()