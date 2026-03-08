class StudentMarks :
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            if(len(self.marks) < 3):
                raise ValueError("Not enough marks to calculate average")
            
            avg = sum(self.marks[-3:]) / 3;
            print("Average of last 3 marks is: ", avg)
        except ValueError as e:
            print(e)

marks_input = input("Enter the marks separated by space: ")
marks_list = list(map(float, marks_input.split()))
student = StudentMarks(marks_list)
student.last_three_avg()

