import time
from multiprocessing import Process

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
process_complex = Process(target=complex_calculation)
process_ask = Process(target=complex_calculation)

process_complex.start()
process_ask.start()
start_multi = time.time()
process_complex.join()
process_ask.join()

print('Two processes total time: ', time.time() - start_multi, '\n\n')
