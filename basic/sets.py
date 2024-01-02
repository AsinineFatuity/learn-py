friends={'Kenny','Scout','Jerry'}
more_friends=set()
new_friend=input("Enter the name of your new friend: ")
more_friends.add(new_friend)
print("These are all your friends: "+str(more_friends.union(friends)))