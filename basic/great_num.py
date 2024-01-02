numbers=[11,2,300,4,50]
great=numbers[0]
index=0
for num in numbers:
    print('----------')
    if numbers[index]>great:
        great=numbers[index]
    else:
        great=great
    index+=1
print(great)