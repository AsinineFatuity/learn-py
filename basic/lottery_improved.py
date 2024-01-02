lottery_numbers = {13, 21, 22, 5, 8}
players=[
         {'name':'Kembo','numbers':{1,3,21}},
         {'name':'Kenny','numbers':{5,9,7}}
        ]
for play in players:
    names=play["name"]
    numbers=play["numbers"].intersection(lottery_numbers)
    print(f"{names} got {len(numbers)} numbers right, that is {numbers}")