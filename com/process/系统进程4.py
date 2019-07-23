import random
from multiprocessing import Pool

import time


def worker():
    for i in range(5):
        print("==========%d======="%i)
        time.sleep(0.5 )



pool = Pool(3)
for i in range(10):
    print("====1======%d=======" % i)
    pool.apply_async(worker)
    # pool.apply(worker)

pool.close()
pool.join()