friends=['Kenny','Scout','Jerry','Nyabuti']
"""
the first variable is the one that acts as a counter regardless of whatever name you give it
thus I should somewhat write counter,friend
"""
for counter,friend in enumerate(friends):
    print(friend)#if this alone then we'll have a tuple
print(list(enumerate(friends)))
#similarly using the zip function:
print(list(zip(friends,(0,1,2,3,4))))
