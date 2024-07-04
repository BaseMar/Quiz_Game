class QuizBrain:
    def __init__(self, q_list, show_restart_callback):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None
        self.show_restart_callback = show_restart_callback

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self, label, buttons):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            question_text = self.current_question.text
            label.configure(text=question_text)
            buttons[0].configure(text=self.current_question.answer_1, command=lambda: self.check_answer(self.current_question.answer_1, label, buttons))
            buttons[1].configure(text=self.current_question.answer_2, command=lambda: self.check_answer(self.current_question.answer_2, label, buttons))
            buttons[2].configure(text=self.current_question.answer_3, command=lambda: self.check_answer(self.current_question.answer_3, label, buttons))
            buttons[3].configure(text=self.current_question.answer_4, command=lambda: self.check_answer(self.current_question.answer_4, label, buttons))
        else:
            label.configure(text=f"You've completed the quiz! \n Final Score: {self.score}/{len(self.question_list)}")
            self.show_restart_callback()

    def check_answer(self, user_answer, label, buttons):
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        self.next_question(label, buttons)
