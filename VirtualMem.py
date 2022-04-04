from Page import Page
from files import read_processes, read_memconfig, read_commands


def isFull(page[] mainMemory):
    for i in range(len(mainMemory[])):
        if mainMemory[i] == '':
            print(str(i) + ' is empty')
            return i
        else:
            return -1


    #Frees a variable ID from a page
def Release(variableId, page[] mainMemory):
    found = False
    #If variable ID is in Main Memory
    for i in range(len(mainMemory)):
        if mainMemory[i].getId == variableId:
            found = True 
            mainMemory[i] = ''
            return true

        #open disk file code here
        if found == False :
            #If variable ID is in Disk Space, remove it
            for i in range(len(mainMemory)):
                if mainMemory[i].getId == variableId:
                    found = True 
                    mainMemory[i] = ''
                    return True




    #Stores page in memory
def Store(self, command): #command is the array that contains the command to be executed.
    if self.isFull:
        print("Virtual Memory is full")
    else:
        store_in_page = Page(command[1], command[2])


