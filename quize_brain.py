class  QuizeBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.secor = 0

    def is_still_has_question(self):
        if len(self.question_list)>self.question_number:
            return True
        else:
            print("\n")
            print("you have completed the quize ")
            print(f"the final  score is {self.secor} / {self.question_number} ")
            return False

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number +=1
        self.user_input =  input(f"  Q{self.question_number}: {self.current_question.text} (true/false)? ").lower()


    def checking_answer(self):
        if self.current_question.answer.lower() == self.user_input:
            print("your got it right !")
            self.secor +=1
        else:
            print("that is wrong answer")
        print(f"the correct answer is {self.current_question.answer}")
        print(f"the current score is {self.secor } / {self.question_number} ")
        print("\n")



