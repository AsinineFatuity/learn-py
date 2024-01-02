import time
import random
import queue
from threading import Thread
counter = 0
job_queue = queue.Queue() #handles things to be printed out
counter_queue = queue.Queue()#handles amounts by which to increase counter

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()#waits till there is an item available in the queue, then locks the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f'New counter value is {counter}','------------'))
        time.sleep(random.random())
        counter_queue.task_done() #unlocks the queue
Thread(target=increment_manager,daemon=True).start()

def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()
Thread(target=printer_manager,daemon=True).start()

def increment_counter_manager():
    time.sleep(random.random())
    counter_queue.put(1)

worker_threads = [Thread(target=increment_counter_manager) for thread in range(10)]

for thread in worker_threads:
    thread.start()
for thread in worker_threads:
    thread.join()

job_queue.join()
counter_queue.join()