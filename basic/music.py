tracks=[
    'The wonder of it all',
    'How great thou art',
    "I'd rather have Jesus",
    'Like a river glorious'
    ]
print("Enter the track to search for\n")
search_for=str(input())
for gen in tracks:
    if search_for in gen:
            print(gen)
    