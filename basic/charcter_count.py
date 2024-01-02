message="love is strong as death;jealousy is cruel as the grave"
count={}
for character in message:
    count.setdefault(character,0)#initialize all the characters to a count of zero
    count[character]+=1 #get the value using the key then increment the key
    """
    The above line could be more clearly read as count[character]=count[character]+1
    """
print(count)