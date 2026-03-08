class StudentScores :
    def __init__(self, marks):
        self.marks = marks

    def highest_last_two(self):
        try:
            if(len(self.marks) < 2):
                raise ValueError("Not enough scores to find highest value")
            
            max_num = max(self.marks[-2:]) ;
            print("Highest score among last two is: ", max_num)
        except ValueError as e:
            print(e)

scores_input = input("Enter the scores separated by space: ")
scores_list = list(map(int, scores_input.split()))
student = StudentScores(scores_list)
student.highest_last_two()

