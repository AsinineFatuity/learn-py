def count_down(n):
    while n > 0:
        yield n
        n -= 1
number_1= count_down(10)
number_2= count_down(20)

print(next(number_1))
print(next(number_2))
print(next(number_1))
print(next(number_2))
