import pprint
message="Fair as the moon and clear as the sun is the lady whose heart has been won"
count={}
for character in message:
    count.setdefault(character,0)
    count[character]+=1
#pprint.pprint(count)
print(pprint.pformat(count))