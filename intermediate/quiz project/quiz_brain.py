class QuizBrain:
    def __init__(self,bank):
        self.questionNumber = 0
        self.questionList = bank
        self.score = 0
    
    def next_question(self):
        ans = input(f"Q.{self.questionNumber+1}: {self.questionList[self.questionNumber].text} (True/False)?: ").lower()
        self.questionNumber += 1
        return ("True" if ans[0]=='t' else "False")
    
    def is_correct(self,ans):
        if (self.questionList[self.questionNumber-1].answer.lower())[0] == ans[0].lower():
            print("Correct! 🥳")
            self.score += 1
        else:
            print("Wrong! 😓")
        print(f"The correct answer was: {self.questionList[self.questionNumber-1].answer}")
        print(f"Your current score is: {self.score}/{self.questionNumber}")
        print("")
        print("")

    def at_end(self):
        if len(self.questionList) == self.questionNumber:
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.questionNumber}")
            return True
        return False