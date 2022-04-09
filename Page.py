from threading import *
from files import *
import threading

mem_config = read_memconfig()

class Page(Thread):
    def __init__(self, variableId, value):
        Thread.__init__(self)
        self.variableId = variableId
        self.value = value
        self.LAST = 0
        self.HIST = [mem_config[1]]
        self.isAvailable = True

    def setAvailable(self, bool):
        self.isAvailable = bool

    def getAvailable(self):
        return self.isAvailable

    def getID(self):
        return self.variableId

    def getValue(self):
        return self.value

    def getLastAccess(self):
        return self.lastAccess

    def setID(self, a):
        self.variableId = a
    
    def setValue(self, a):
        self.value = a

    def setLastAccess(self, a):
        self.lastAccess = a

    def setLast(self, a):
        self.LAST = a

    def getLast(self):
        return self.LAST

    def setHist(self, index, a):
        self.HIST[index] = a
    
    def getHist(self, index):
        return self.HIST[index]




    def print(self):
        print("Variable id is: " + str(self.variableId))
        print("String value is: " + str(self.value))
        print("Last Access was on " + str(self.lastAccess))