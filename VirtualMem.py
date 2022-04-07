import re

from pip import main
from Page import Page
from files import read_processes, read_memconfig, read_commands
from diskspace import read_disk, vm, remove

mem_config = read_memconfig()


def LookUp(variableId, time, mainMemory):
    found = False
    read_array = read_disk()
        
    #Checks in Main Memory first to find it
    #If it does, then returns the variable Id
    for i in range(len(mainMemory)):
        PageLookUp = mainMemory[i]
        if PageLookUp.getID() == variableId:
            return variableId
        else:
            continue
    for j in range(len(mainMemory)):
        PageLookUp = mainMemory[j]
        if read_array[j][0] == PageLookUp.getID():
            if PageLookUp.getAvailable() == True:
                PageLookUp.setID(variableId)
                PageLookUp.setValue(read_array[j][1])
                remove(j)
            else: #LRU-K algorithm
                if (time - PageLookUp.getLast()) < mem_config[2]:
                    PageLookUp.setLast(time)
                elif (time - PageLookUp.getLast()) > mem_config[2]:
                    lcp = PageLookUp.getLast() - PageLookUp.getHist(1)
                    for  i in range(mem_config[1], 0, -1):
                        PageLookUp.setHist(i, PageLookUp.getHist((i - 1 + lcp)))
                    PageLookUp.setLast(PageLookUp.getHist(1))
                    for m in range(1, mem_config[0]):
                        if PageLookUp.getLast() - PageLookUp.getHist(1) > mem_config[2]:
                            temp = mainMemory[m]
                        if temp.get



                    
            




        
        
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
            
        
    




