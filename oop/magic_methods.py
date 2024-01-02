class Garage:
    def __init__(self) -> None:
        self.car = []
    def __len__(self) -> int:
        return len(self.car)
    def __getitem__(self,i):
        return self.car[i]
    #all classes should have repr and str classes (prioritize repr over str though when you want to define just one of them)
    def __repr__(self) -> str:
        #returns a string that defines the object hence with that string we can recreate that object fully
        return f'<Garage {self.car}>'
    def __str__(self) -> str:
        #returns a string that gives descriptive data to the user
        return f'Garage with {len(self)} cars'
    
ford = Garage()
ford.car.append("Focus")
ford.car.append("Fiesta")
#the length of my car list
print(len(ford))
#the list of my ford cars
print(ford.car)
#the index of any ford car
print(ford[0])
#with the getitems dunder method defined, we can now loop over our objects (here we have mercedes)
mercedes = Garage()
mercedes.car.append("B-Class")
mercedes.car.append("C-Class")
mercedes.car.append("CLA")
mercedes.car.append("CLS")

for car in mercedes:
    print(car,sep=",")

print(mercedes)