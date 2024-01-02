#student object can store data
class Student:
    def __init__(self,new_name,new_grade) -> None:
        #name and grade live inside the new blank object self (can be called anything though apart from self)
        self.name = new_name
        self.grade = new_grade
    def average(self):
        return sum(self.grade)/len(self.grade)

#creating an oject
student_one = Student('Frank',(80,94,90,90,87))
print(student_one.average())
print(student_one.__class__)