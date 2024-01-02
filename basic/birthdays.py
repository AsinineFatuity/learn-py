birthdays={
'Nyareki':'July 27','Kenny':'May 5','Kembo':'July 23','Scout':'March 11','Trizah':'May 26','Brenda':'May 23', 'Vivian':'September 16',
'Towett':'December 6','Joan':'December 11','Audrey':'August 10','Onditi':'Feb 21','Trevor':'Feb 24','Eva':'Nov 16'
}
while True:
    print("Enter the name or blank to quit")
    name=input()
    if name==' ':
        break
    if name in birthdays:
        print(f"{name}'s birthday is on {birthdays[name]}")
    else:
        print("I do not have the birth date for "+name+ '\n' 
        +"Please enter their birth date (format is Month day e.g January 5)")
        bdate=input()
        birthdays[name]=bdate
        print("Birthdays database updated successfully")
        
