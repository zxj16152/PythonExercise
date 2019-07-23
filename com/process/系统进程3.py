
from multiprocessing import Process

import time


class MyProcess(Process):
    def __init__(self,args):
        Process.__init__(self)
        self.args=args


    def run(self):
        while True:
            print("-----1-----")
            time.sleep(1)
            print("-----args=%s----"%self.args)


process = MyProcess("你好")
process.start()
