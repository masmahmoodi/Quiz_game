from quize_model import  Question
from data import question_data
from quize_brain import  QuizeBrain

question_bank = [

]



for key in question_data:
   question = key["text"]
   answer = key["answer"]
   appending = Question(question,answer)
   question_bank.append(appending)
quize = QuizeBrain(question_bank)
off = False
while quize.is_still_has_question():
   quize.next_question()
   quize.checking_answer()