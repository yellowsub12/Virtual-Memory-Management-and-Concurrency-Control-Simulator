from threading import Thread

class Page(Thread):
    def __init__(self, variableId, value, lastAccess):
        Thread.__init__(self)
        self.variableId = variableId
        self.value = value
        self.lastAccess = lastAccess


    def getID(self):
        return self.variableId

    def getValue(self):
        return self.value

    def getLastAccess(self):
        return self.lastAccess


    def print(self):
        print("Variable id is: " + str(self.variableId))
        print("String value is: " + str(self.value))
        print("Last Access was on " + str(self.lastAccess))


