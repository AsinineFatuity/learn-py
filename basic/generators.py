def square_numbers(nums):
    for num in nums:
        yield(num*num)
to_square_list = [1,2,3,4,5,6,7,8,9]
squared_result = square_numbers(to_square_list)
for num in squared_result:
    print(num)
print('------------------------------')
#using generator comprehension
comprehended_squared = (x*x for x in [1,2,3,4,5,6,7,8,9])
for num in comprehended_squared:
    print(num)
#generators perform better than lists in terms of memory and speed