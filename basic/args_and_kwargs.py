#wanted to show that the args can actually be analogous to operator overloading since it accepts multiple arguments though
#it is just one function
def print_names(*arguments):
    print(*arguments)#unpack the list or tuple of names sent and then print
#to use the unpacking operator for dictionaries, you ensure that the function parameters are the same as the key
#and also that you use ** instead of * to unpack the dictionary values. * will only unpack the keys.
def print_names_dict(**kwargs):
    print(kwargs)
*names_1,='Kembo','Frank','Otieno' #have many names stored in one variable
print_names(names_1)
names_2={'a':'Kembo','b':'Frank','c':'Otieno'}
print_names_dict(**names_2)
print_names('Frank')