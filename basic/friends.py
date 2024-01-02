my_friends=['Kenny','Scout','Jerry','Nyabuti']
while True:
    print('Guess the names of my friend')
    friend=input()
    if friend not in my_friends:
        print('I do not have a friend called '+friend)
        print('But these are all my friends ):')
        for friendz in my_friends:
            print(''+ friendz)
        break
    else:
        for f in range(len(my_friends)):
            if my_friends[f]==friend:
                print(friend+' is my number '+str(f+1)+' friend')
                

            