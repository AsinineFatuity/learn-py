"""These are threads which cannot be interrupted until they finish their task as they perform atomic operations"""
"""Additionally, my attempt to use a lock also does not work as they are now sequentially printed out but not to 10"""
import threading
import time
import random

from concurrent.futures import ThreadPoolExecutor
from threading import Thread
#counter = 0 #this is the shared state variable that is accessed and updated
class TestUpdater():
    def __init__(self) -> None: 
        self.counter = 0     
        self._lock = threading.Lock()
    def increment_counter(self):
        with self._lock:
            local_copy = self.counter
            local_copy += 1
            time.sleep(random.random())
            self.counter = local_copy
            print(f"New Counter Value is: {self.counter}",'-----------------------------')
            time.sleep(random.random())
        return self.counter
test_updater = TestUpdater()
for x in range(22):
    #with ThreadPoolExecutor(max_workers=2) as t:
    t = Thread(target=test_updater.increment_counter,daemon=True)
    time.sleep(random.random())
    t.start()
    #it is thus a background thread and will exit after the main thread of this program exits

