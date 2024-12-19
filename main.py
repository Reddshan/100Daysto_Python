from question_model import Question
from data import question_data
from quiz_brain import quizBrain
### declaring open question bank
ques_bank=[]
for ech_dict in question_data:
    ques_bank.append(Question(ech_dict['question'],ech_dict['correct_answer']))
quzbra=quizBrain(ques_bank)
quzbra.next_question()
print("Quiz is finished")
print(f"Final Score is : {quzbra.score} out of {len(ques_bank)}  questions")

#print(ques_bank)
#print