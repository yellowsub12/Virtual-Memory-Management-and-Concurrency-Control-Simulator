import re
from Page import Page
from files import read_processes, read_memconfig, read_commands
from diskspace import read_disk, vm, remove


    #reminder, main memory is like an array where pages are elements
    #you don't add or remove pages, you only associate a variable ID and value to every page


def LookUp(variableId, time, mainMemory):
    found = False
    read_array = read_disk()
    j = 0
        
    #Checks in Main Memory first to find it
    #If it does, then returns the variable Id
    for i in range(len(mainMemory)):
        PageLookUp = mainMemory[i]
        if PageLookUp.getID() == variableId:
            found = True 
            return variableId
        elif read_array[j][0] == PageLookUp.getID():
            if PageLookUp.getAvailable() == True:
                PageLookUp.setID(variableId)
                PageLookUp.setValue(read_array[j][1])
                remove(j)
            else: #LRU-K algorithm
                if time - PageLookUp.getLast():
                    
            




        
        
        #return -1 


    #If not

    #Determines if main memory has free spot
def isFull(mainMemory):
        for i in range(len(mainMemory)):
            if mainMemory[i] == '':
                return i

        else:
            return -1


    #Frees a variable ID from a page
def Release(variableId, mainMemory):
        found = False
        #If variable ID is in Main Memory
        for i in range(len(mainMemory)):
            if mainMemory[i][0] == variableId:
                found = True 
                mainMemory[i] = ''
                return True


        #open disk file code here
        #if found == False :
            #If variable ID is in Disk Space, remove it
            
        #If neither condition above fulfilled, return false to let program know it failed
        #return False
        





    #Stores variable ID and value in page memory
def Store(variableId, value, mainMemory):
        
        #Stores Id and value if there's memory
        if (VirtualMem.isFull(mainMemory) != -1):
            mainMemory[VirtualMem.isFull(mainMemory)] = [variableId,value]
            #store it in Disk space as well, code for that here
        #else:
            #open vm txt and add into it 
            
        
    




