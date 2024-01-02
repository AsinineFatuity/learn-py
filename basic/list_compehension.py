friends=["Kenny","Scout","Jerry","Nyabuti"]
friend=input("Enter the name of your friend: ")
if friend.lower() in [_.lower()for _ in friends]:
    print(f"{friend.title()} is one of your friends")#for title casing