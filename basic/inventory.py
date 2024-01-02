"""
The following program manipulates lists together with dictionaries by adding list items onto the dictionary
"""

myProperty={'Laptop':1,'Phone':2,'Mouse':1,'Earphone':1,'Arduino':1}
myWishList=['Mouse','Phone','Laptop']
def displayProperty(myDict):
    total=0
    print("Technological Items Owned:\n")
    for key,value in myDict.items():    
        print(str(value)+' '+key)
        total+=value
    print("Total Technological Items Owned "+str(total))
def addToInventory(myDict,wishList):
    for items in wishList:
        if items in myDict.keys(): #check if the items in my wish list are keys in my dictionary
            myDict[items]+=1#increment the value of the key
    #print(myDict.items()) confirms that the code actually worked in that the items were incremented
    displayProperty(myDict) #this finaly send them up there so that everything is added up
addToInventory(myProperty,myWishList)