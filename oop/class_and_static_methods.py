#when we use these decorators, our methods do not take the object (self) as the first argument rather they take the class (in the case of classmethod) or not (in the case of staticmethod)
#usually we use staticmethod when we will not inherit that class so that we do not need to dynamically refer to our class else it is always advisable to use classmethod so that we do not lose that functionality
class Student:
    def __init__(self,name,school) -> None:
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks)/len(self.marks)
omia = Student('Sylvia Omia',"Homabay Children's Home Academy")
omia.marks.append(80)
omia.marks.append(90)
print(omia.average())
#class method takes the class itself as parameter and accesses the object in the class
class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
foo = Foo()
print(foo.hi())
#static method does not in anyway relate to the class but just has to be within it hence it does not take any class/object as argument
class Bar:
    @staticmethod
    def hi():
        print("No parameters taken")
bar = Bar()
print(bar.hi())
