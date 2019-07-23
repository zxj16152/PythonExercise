import os
import time
from multiprocessing import Process


def test():
    while True:
        print("-----1--------")
        time.sleep(1)


process = Process(target=test)
process.start()

while True:
    print("-------2-------")
    time.sleep(1)


