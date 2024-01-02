import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
#here is the code for the looping and writing out of the intersections
winner_len=len(players[0]['numbers'].intersection(lottery_numbers))
#here is the winners list and numbers matched that are to be populated
winner_list=[]
for plist_it in players:
    print('Here are the details for everyone: ')
    print(plist_it['name']+' '+str(len(plist_it['numbers'].intersection(lottery_numbers))))
    if len(plist_it['numbers'].intersection(lottery_numbers))>winner_len:
        winner_len=len(plist_it['numbers'].intersection(lottery_numbers))
        winner_name=plist_it['name']
    if len(plist_it['numbers'].intersection(lottery_numbers))==winner_len and winner_len!=0:
        winner_name=plist_it['name']
        winner_list.append(winner_name)
        num_matched=winner_len       
    else:
        winner_len=len(players[0]['numbers'].intersection(lottery_numbers))
        winner_name=players[0]['name']
print("--------Beethoven's 5th Symphony------")
print("The winner is: "+winner_name+' '+str(winner_len))
print(winner_name+" won "+str(100*winner_len))
print("--------Beethoven's 9th Symphony------")
print("all these are winners: "+str(winner_list)+" and each won "+str(num_matched*100))
# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
