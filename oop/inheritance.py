class Student:
    def __init__(self,name,school) -> None:
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)
class WorkingStudent(Student):
    def __init__(self, name, school,salary) -> None:
        super().__init__(name, school)
        self.salary = salary
    @property #done only when a function takes the argument self only
    def monthly_salary(self):
        return round(self.salary/12 * 100)

kembo = WorkingStudent('Kembo','UON',55000)
kembo.marks.append(78)
kembo.marks.append(80)
print(kembo.average())
print(kembo.monthly_salary)