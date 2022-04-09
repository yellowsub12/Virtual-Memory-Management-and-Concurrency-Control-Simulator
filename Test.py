
from threading import *
import time
import threading

class CPUPainter():
    def __init__(self, one, two, three):
        self.i = one
        self.x = two
        self.z = three

    def getOne(self):
        time.sleep(2)
        print(self.i)
        return self.i

    def getTwoz(self):
        def getTwo(self):
            time.sleep(2)
            print(str(self.x))
        def run(self):
            t = threading.Thread(target = getTwo(self))
            t.start()
        run(self)


        



d = CPUPainter(1,2,3)
b = CPUPainter(1,4,3)

d.getTwoz()
print(threading.active_count())
b.getTwoz()
print(threading.active_count())











