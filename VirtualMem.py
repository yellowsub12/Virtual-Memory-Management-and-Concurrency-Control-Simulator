from Page import Page

class VirtualMem():

    #Determines if main memory has free spot
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
                    return true




    #Stores page in memory
    def Store(Page.variableId, Page.value, time, mainMemory[]):
        
        if()


