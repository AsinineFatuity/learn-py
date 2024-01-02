#this illustrates lambda functions and also the bargain between if statements and dictionaries for functions
operation_functions = {
    "average":lambda seq:sum(seq)/len(seq),
    "total":sum,
    "max":max
}
#the students dictionary
students = [
    {"name":"Oswago","grades":(94,78,80,90,85)},
    {"name":"Albright","grades":(100,90,80,80,86)},
    {"name":"Frank","grades":(80,94,90,90,87)},
    {"name":"Omia","grades":(80,80,88,90,90)},
]
#loop through each of the students to obtain name and grades
for student in students:
    name = student["name"]
    grades = student["grades"]
    print(f"Student: {name}")
    operation = input("Enter the operation on their marks: 'average' or 'total' or 'max' ")
    try:
        operation_function = operation_functions[operation]
    except KeyError:
        print("Operation does not exist")
        operation = input("Enter the operation on their marks: 'average' or 'total' or 'max' ")
        operation_function = operation_functions[operation]

    print(operation_function(grades))
