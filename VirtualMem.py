import re

from pip import main
from Page import Page
from files import *
from diskspace import *

mem_config = read_memconfig()


def LookUp(variableId, time, mainMemory):
    found = False
    read_array = read_disk()
    lower_temp = 0
    condition_check = 0
    temp_page = 1000000000
    temp_disk = []
        
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
                        x = mainMemory[m]
                        if x.getLast() - x.getHist(1) > mem_config[2]:
                            if lower_temp.getHist(mem_config[1]) == x.getHist(mem_config[1]):
                                if lower_temp.getHist(1) < x.getHist(1):
                                    lower_temp = x
                                else:
                                    lower_temp = lower_temp
                            else:
                                lower_temp = x
                            condition_check = condition_check + 1
                        elif condition_check == 0:
                            for n in range(1,mem_config[0]):
                                x = mainMemory[n]
                                if x.getHist(1) < temp_page:
                                    temp_page = x.getHist(1)
                                else:
                                    continue
                            for p in range(0, mem_config[0]) :
                                if mainMemory[p].getHist(1) == temp_page:
                                    for z in range(len(read_array)):
                                        if variableId == read_array[z][0]:
                                            temp_disk = read_array[z]
                                            pass_vm = [mainMemory[p].getID(),mainMemory[p].getValue()]
                                            vm_replace(z,pass_vm)
                                            mainMemory[p].setId(temp_disk[0]) 
                                            mainMemory[p].setValue(temp_disk[1])
                                            mainMemory[p].setHist(1,time)
                                            for yup in range(1,mem_config[1]):
                                               mainMemory[p].setHist(yup,0)
                                            mainMemory[p].setLast(time)
                                            return True



                #Code for pt 4 
                #When a page is first used, or was just replaced, it's associated information is initialized as below
                #LAST(p) and HIST(p)[1] are set to the time stamp of that usage/replacement
                #HIST(p)[i], for i, 1<i<K< are set to zero
               
                

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
        diskspace = read_disk()

        #If variable ID is in Main Memory
        for i in range(len(mainMemory)):
            if mainMemory[i][0] == variableId:
                found = True 
                mainMemory[i] = ''
                return True
        #open disk file code here
        if found == False :
            #If variable ID is in Disk Space, remove it
            for i in range(len(diskspace)):
             if diskspace[i][0] == variableId:
                found = True 
                remove(i)
                return True
        
        #If still falls, return found which is gonna be still false
        #to let program know it was false
        return found
        





    #Stores variable ID and value in page memory
def Store(variableId, value, mainMemory):
        
        #Stores Id and value if there's memory
        if (isFull(mainMemory) != -1):
            mainMemory[isFull(mainMemory)] = [variableId,value]
        #otherwise stores it in disk space
        else:
            vm([variableId,value])
            
        
    




