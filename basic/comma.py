def comma(someList):
    last_item=someList[-1]#save the last item on the list
    del(someList[-1])#then delete it from the list
    str_list=''#the empty string where I will store my output
    for n in range(len(someList)):
        str_list+=someList[n]+','#make the list items comma separated
    str_list+='and '+last_item #then add the last item with an and before it
    print(str_list)#print the manipulated list
list=[]#this empty list will contain my input, if this is declared inside the while loop, only the last value will be stored
#as it will be initialized every time
while True:#to allow multiple entries
    list_item=input("Enter the list items or Q to Quit:\n")
    if list_item=='Q':
        print("See you next time!")
        break   
    else:
        list.append(list_item)   
print(list)
comma(list)





