class StudentPerformance:
    def __init__(self, marks):
        self.marks = marks

    def score_difference(self):
        try:
            if(len(self.marks) < 2):
                raise ValueError("No scores available to calculate difference")
            
            diff = self.marks[-1] - self.marks[0]
            print("Difference between last and first score is: ", diff)
        except ValueError as e:
            print(e)

scores_input = input("Enter the scores separated by space: ")
scores_list = list(map(int, scores_input.split()))
student = StudentPerformance(scores_list)
student.score_difference()

