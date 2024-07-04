import customtkinter
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random

customtkinter.set_appearance_mode("Dark")


class QuizGame(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Quiz Game")
        self.geometry(f"{800}x{600}")
        self.resizable(False, False)

        # configure grid
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # field for question
        self.upper_frame = customtkinter.CTkFrame(self, width=800, corner_radius=0)
        self.upper_frame.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        self.q_label = customtkinter.CTkLabel(self.upper_frame, text="Question", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.q_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.buttons = []
        for i in range(4):
            button = customtkinter.CTkButton(self, width=150)
            button.grid(row=2, column=i, padx=20, pady=10)
            self.buttons.append(button)

        self.restart_button = customtkinter.CTkButton(self, text="Restart", command=self.restart_quiz)
        self.restart_button.grid(row=3, column=1, columnspan=2, padx=20, pady=20)
        self.restart_button.grid_remove()

        self.initialize_quiz()

    def initialize_quiz(self):
        question_bank = []
        for index, question in question_data.iterrows():
            new_question = Question(
                q_text=question["Text"],
                q_asw_1=question["answer1"],
                q_asw_2=question["answer2"],
                q_asw_3=question["answer3"],
                q_asw_4=question["answer4"],
                q_corr_answer=question["corr_answer"]
            )
            question_bank.append(new_question)

        random.shuffle(question_bank)

        self.quiz = QuizBrain(question_bank, self.show_restart_button)
        self.restart_button.grid_remove()
        self.quiz.next_question(self.q_label, self.buttons)

    def restart_quiz(self):
        self.quiz.question_number = 0
        self.quiz.score = 0
        self.initialize_quiz()

    def show_restart_button(self):
        self.restart_button.grid()


if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
