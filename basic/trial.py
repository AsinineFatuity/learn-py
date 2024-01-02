# players = [
#     {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
#     {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
#     {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
#     {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
# ]
# for pl in players:
#     print(pl['name'])
theBoard={
    'top-L':' ','top-M':' ','top-R':' ',
    'mid-L':' ','mid-M':' ','mid-R':' ',
    'low-L':' ','low-M':' ','low-R':' '
}
for value in theBoard.values():
    if value==' ':
        print('True')