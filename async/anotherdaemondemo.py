"""This is from Real Python and sort of clarifies my own putting the ox before the cart"""
import logging

import threading

import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    #time.sleep(2) 
    input("Enter name: ")
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    #allows us to log in the terminal
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")                
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,),daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    #the .join will ensure that any thread, daemon or not finishes execution
    x.join()
    logging.info("Main    : all done")