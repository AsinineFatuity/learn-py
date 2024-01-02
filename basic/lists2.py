#I just want to enter all the names of people who matter to me and then list them
people_matter=[]
while True:
    print('Enter person '+str(len(people_matter)+1)+' who matters to you, Q to quit')
    people=input()
    if people=='Q':
        break
    people_matter.append(people)
people_matter[0]='Three Living Persons of the heavenly trio'#to ensure I am reminded of priorities
#print('The following people matter to you\n'+str(people_matter[:]))
print('The following people matter to you')
for names in people_matter:
    print(''+names)
    



