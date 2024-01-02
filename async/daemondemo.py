from threading import Thread
import time
import logging
# creating a function
def thread_1():					
    for i in range(3):
        print("This is a daemon thread")
        input("Enter name: ")

# creating a thread
T = Thread(target = thread_1)

# change T to daemon
T.setDaemon(True)				
#starting of Thread T
T.start()	
T.join()					
time.sleep(5)
logging.info('this is Main Thread')