"""This is an annotated program from RealPython to show case the race conditons that come about when we multithread in python and also how to fix them"""
import logging,time
from concurrent.futures import ThreadPoolExecutor
import threading

class FakeDatabase:
    def __init__(self):
        self.value = 0
        #we now add a lock to this initializer method
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        #notify the user that I am actually locking this thread(giving it the hall pass as it were)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            local_copy = self.value
            local_copy += 1
            #this delay allows thread 2 to begin but we have not yet updated the value using thread 1 that is asleep
            time.sleep(0.1)
            #by using the += sign instead of = we avoid overwriting, or we can also eliminate the delay
            #however, this is a primitive way of really solving this issue because it is local to this and besides it does not solve the full spectrum of complexities that
            #come with the operating system handling the threads for us. we now use lock feature instead
            self.value = local_copy
            #notify user that we are about to release the lock
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    database = FakeDatabase()

    logging.info("Testing update. Starting value is %d.", database.value)
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
