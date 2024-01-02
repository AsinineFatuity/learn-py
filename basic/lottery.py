lottery_numbers = {13, 21, 22, 5, 8}
player_1={'name':'Kembo','numbers':{1,3,21}}
player_2={'name':'Kenny','numbers':{5,9,7}}
got_right_1=player_1['numbers'].intersection(lottery_numbers)
got_right_2=player_2['numbers'].intersection(lottery_numbers)
len_right_1=len(player_1['numbers'].intersection(lottery_numbers))
len_right_2=len(player_2['numbers'].intersection(lottery_numbers))
print("Hello "+player_1['name']+" you got "+str(len_right_1)+" number(s) right"\
    "they are: "+str(got_right_1))
print("Hello "+player_2['name']+" you got "+str(len_right_2)+" number(s) right"\
    "they are: "+str(got_right_2))
