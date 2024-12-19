class quizBrain:
    def __init__(self,ques_list):
        self.question_number=0
        self.quest_list=ques_list
        self.score=0
    def next_question(self):
        score = 0
        for i in range(0,len(self.quest_list)):
           question_flag=input(f"Q.{self.question_number+1}:{self.quest_list[i].question}. (True/False)?:")
           self.check_answer(question_flag, self.quest_list[i].answer)
           self.question_number+=1
    def check_answer(self,user_ans,correctans):
        if user_ans==correctans:
            print("You Got it Right.")
            self.score += 1
            print(f"Your Score is {self.score}/{len(self.quest_list)}")
        else:
            print("You Got it Wrong.")
            print(f"Your Score is {self.score}/{len(self.quest_list)}")
        print(f"The Correct Answer is :{correctans}")
        print("\n")