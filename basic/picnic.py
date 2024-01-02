allFood={
    'Nyareki':{'chapati':10,'smoothie':4},
    'Trizah':{'cake':1,'juice':2},
        }
def totalPicnic(all_Food,food_item):
    total=0 #to calculate the total number of items
    for key,value in all_Food.items():
        total+=value.get(food_item,0)
    return total #if this return statement is inside the loop, it will return after only the first food items
print("We have the following items for the picnic:\n")
print("-cake "+str(totalPicnic(allFood,'cake')))
print("-juice "+str(totalPicnic(allFood,'juice')))
print("-chapati "+str(totalPicnic(allFood,'chapati')))
print("-smoothie "+str(totalPicnic(allFood,'smoothie')))
