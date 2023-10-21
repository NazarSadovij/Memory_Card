class Question:
    def __init__ (self, qestion, right_ans, wrong_ans_1, wrong_ans_2, wrong_ans_3):
        self.qestion  = qestion
        self.right_ans = right_ans
        self.wrong_ans_1 = wrong_ans_1
        self.wrong_ans_2 = wrong_ans_2
        self.wrong_ans_3 = wrong_ans_3

        self.attemps = 0
        self.correct = 0

        self.is_active = True

    def got_right(self):
        self.correct += 1
        self.attemps += 1

    def got_wrong(self):
        self.attemps += 1


class QuestionView():
    def __init__ (self, qestion_model, question, right_ans, wrong_ans_1, wrong_ans_2, wrong_ans_3):

        self.question_model = question

        self.question  = question
        self.right_ans = right_ans
        self.wrong_ans_1 = wrong_ans_1
        self.wrong_ans_2 = wrong_ans_2
        self.wrong_ans_3 = wrong_ans_3

    def change (self, qestion_model):
        self.qestion_model = qestion_model

    
    def show (self):
        self.qestion.setText(self.qestion_model.qestion)
        self.right_ans.setText(self.qestion_model.right_ans)
        self.right_ans.setText(self.qestion_model.wrong_ans_1)
        self.right_ans.setText(self.qestion_model.wrong_ans_2)
        self.right_ans.setText(self.qestion_model.wrong_ans_3)
