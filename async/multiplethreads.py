import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    #this shows that even if I had to wait for ages for my thread to finish, once I join it it must execute before I finish the main thread
    #this can be illustrated using an input that waits indefinitely instead of a time delay that we have control over
    #input("Enter your name: \n")
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()
    for index in range(0,3):#just so that I have my threads indexed from 1
        logging.info("Main: create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main: before joining thread %d.", index)
        thread.join()
        logging.info("Main: thread %d done", index)
