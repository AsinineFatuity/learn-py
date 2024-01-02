import time
from concurrent.futures import ProcessPoolExecutor
def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single process total time: ', time.time() - start, '\n\n')

#multiple processes (running on different cores), this is however not suitable to use when a process waits for a resource such as input console.
#we now use the process pool to handle all the starting
start_multi = time.time()
#pool = ProcessPoolExecutor(max_workers=2)
with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
#in case I will need to end a process and return it back to the pool once it has finished running, declare the process as a variable without the with (see line 26)


print('Two processes total time: ', time.time() - start_multi, '\n\n')
