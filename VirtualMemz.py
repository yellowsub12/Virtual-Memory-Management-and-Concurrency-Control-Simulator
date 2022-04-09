import re

from pip import main
from Page import Page
from VirtualMem import isFull
from files import *
from diskspace import *

mem_config = read_memconfig()


def LookUp(variableId, time, mainMemory):
    found = False
    read_array = read_disk()
    condition_check = 0
    temp_page = 1000000000
    temp_disk = []
    PagesThatPass = [] 
    PagesThatPassCounter = 0 
    PagesThatPassDuplicates = []
    smallestHist = 100000000000000
    smallestHistPage = 0 

    #Checks in Main Memory first to find it
    #If it does, then returns the variable Id
    for i in range(len(mainMemory)):
        if mainMemory[i].getID() == variableId:
            return variableId
        else:
            continue
    if (isFull(mainMemory) != -1) :    
        for i in range(len(read_array)):
            if read_array[i][0] == variableId:
                mainMemory[i].setID(variableId)
                mainMemory[i].setValue(read_array[i][1])
                remove(i)
    elif (isFull(mainMemory) == -1 )  :
        #When a page replacement is needed
        for m in range(0, mem_config[0]):
            #Of all the pages that have Last(p) - Hist(p)[1] > time-out
            if mainMemory[m].getLast() - mainMemory[m].getHist(1) > mem_config[2]:
                #Choose the one with the smallest value

                PagesThatPass[PagesThatPassCounter] = mainMemory[m]
                PagesThatPassCounter += 1 
        # There aren't any pages that pass
        if PagesThatPassCounter==0 :
            for i in range(len(mainMemory)):
                k = i + 1
                for j in range (len(mainMemory)):
                    if mainMemory[i].getHist(1) < smallestHist:
                        smallestHist = mainMemory[i].getHist(1)
            for i in range(len(mainMemory)):
                if mainMemory[i].getHist(1) == smallestHist:
                    smallestHistPage = mainMemory[i]
            #Place replacement algorithm here, whereby smallestHistPage is the page to be booted
            for z in range(len(read_array)):
                            if variableId == read_array[z][0]:
                                temp_disk = read_array[z]
                                pass_vm = [smallestHistPage.getID(),smallestHistPage.getValue()]
                                vm_replace(z,pass_vm)
                                smallestHistPage.setId(temp_disk[0]) 
                                smallestHistPage.setValue(temp_disk[1])
                                smallestHistPage.setHist(1,time)
                                for yup in range(1,mem_config[1]):
                                    smallestHistPage.setHist(yup,0)
                                    smallestHistPage.setLast(time)
                                    return True
        
        # If there are pages that pass, also checks for duplicates and finds the smallest duplicate
        else :
            for i in range(len(PagesThatPass)):
                k = i+1
                for j in range (k,len(PagesThatPass)):
                            if PagesThatPass[i].getHist(mem_config[2]) == PagesThatPass[j].getHist(mem_config[2]) and PagesThatPass[i].getHist(mem_config[2]) not in PagesThatPassDuplicates.getHist(mem_config[2]):
                                PagesThatPassDuplicates.append(PagesThatPass[i])
            for i in range(len(PagesThatPassDuplicates)):
                    k = i + 1
                    for j in range (len(PagesThatPassDuplicates)):
                        if PagesThatPassDuplicates[i].getHist(1) < smallestHist:
                            smallestHist = PagesThatPassDuplicates[i].getHist(1)
            for i in range(len(PagesThatPassDuplicates)):
                    if PagesThatPassDuplicates[i].getHist(1) == smallestHist:
                        smallestHistPage = PagesThatPassDuplicates[i]
            #Place replacement algorithm here, whereby smallestHistPage is the page to be booted
            for z in range(len(read_array)):
                            if variableId == read_array[z][0]:
                                temp_disk = read_array[z]
                                pass_vm = [smallestHistPage.getID(),smallestHistPage.getValue()]
                                vm_replace(z,pass_vm)
                                smallestHistPage.setId(temp_disk[0]) 
                                smallestHistPage.setValue(temp_disk[1])
                                smallestHistPage.setHist(1,time)
                                for yup in range(1,mem_config[1]):
                                    smallestHistPage.setHist(yup,0)
                                    smallestHistPage.setLast(time)
                                    return True






                
                #return -1 otherwise

                #Code for pt 4 
                #When a page is first used, or was just replaced, it's associated information is initialized as below
                #LAST(p) and HIST(p)[1] are set to the time stamp of that usage/replacement
                #HIST(p)[i], for i, 1<i<K< are set to zero
               
               for i in range(len(mainMemory)):
                if mainMemory[i].getID() == variableId:


                

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
            
        
    




