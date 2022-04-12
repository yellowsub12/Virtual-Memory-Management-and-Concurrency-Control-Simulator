from argparse import Action
from hashlib import new
from itertools import count
from multiprocessing import process
from multiprocessing.connection import wait
from Process import Process
import queue
import threading
import os
from MemoryManager import MemoryManager
from files import *
from diskspace import *
import random
import sys

def main():
    global clock
    clockthread = threading.Timer(interval, main).start()
    if clock > 0 :
        print("Clock: %d" % clock)
    t2 = threading.Thread(target=scheduler)
    clock = clock + 1000
    t2.start()
    t2.join()



def scheduler():
    global clock
    global count_processes
    global expiry_count
    expired_processes = []
    global processToExecute
    randomWaitTime = 0
    randomTimes = [100,200,300,400,500,600,700,800,900,1000] #random time in ms for process execution
    count_processes = 0
    count_commands = 0

    while True:
        if count_processes < int(getNumProcesses()):  #As long as the count of processes is not bigger than the number of processes
            x = processes[count_processes] #initialize the new processes
            if int(x.getArrivalTime()) <= clock : #current time of the clock:
                if ActiveQueue.full(): #put in acive queue which is sized only to the number of cores.
                    print("Clock: " + str(x.getArrivalTime()) + ", Process " + str(x.getID()) +  ": Started.")
                    InactiveQueue.put(x)
                    count_processes = count_processes + 1
                else: #else put in the inactive
                    print("Clock: " + str(x.getArrivalTime()) + ", Process " + str(x.getID()) + ": Started.")
                    ActiveQueue.put(x)
                    count_processes = count_processes + 1

        while not ActiveQueue.empty(): #as long as the active queue has a process inside, execute
            processToExecute = ActiveQueue.get() #get first process in queue
            if count_commands == len(listcommands): #when all the commands are done, return to first command
                count_commands = 0
            if count_commands <= len(listcommands):#since not all commands have been executed
                line = listcommands[count_commands]
                x = line.split() #gbreak the command into an array to use as varibales.
                if len(x) == 2: #in case we only have a variable id to use and no value to avoid array out of range
                    randomWaitTime = random.choice(randomTimes) #get a random waiting time for the process
                    clock = clock + randomWaitTime #update clock
                    MemoryManager(x[0], x[1], 0, clock, processToExecute) #call memory manager and the execute one of the three function accordingly
                    if int(processToExecute.getBurst()) < randomWaitTime: #check if process needs to be terminated
                        processToExecute.setBurst(0) #burst is equal to zero now
                        print("Clock: " + str(clock) + ", " + str(processToExecute.getID()) + ": Finished")
                        expired_processes.append(processToExecute) #put expired process in the discard array
                        expiry_count = expiry_count + 1 #increase the count of expired process
                        if expiry_count > (int(getNumProcesses()) - 1): #check if all processes are done and terminate the program
                            print("Program Completed!")
                            f.close()
                            os._exit(0)
                        count_commands = count_commands + 1 #increase the command count
                        continue
                    else: #if it is not due for termination
                        processToExecute.setBurst((int(processToExecute.getBurst()) - randomWaitTime)) #update burst time
                        InactiveQueue.put(processToExecute) #put in inactive queue
                else: #same logic as above but executed when the command to be executed uses a variable as well
                    randomWaitTime  = random.choice(randomTimes)
                    clock = clock + randomWaitTime
                    MemoryManager(x[0],x[1],x[2],clock,processToExecute)
                    if int(processToExecute.getBurst()) < randomWaitTime:
                        processToExecute.setBurst(0)
                        print("Clock: " + str(clock) + ", " + str(processToExecute.getID()) + ": Finished")
                        
                        expired_processes.append(processToExecute)
                        expiry_count = expiry_count + 1

                        if expiry_count > (int(getNumProcesses()) - 1): #check if all processes are done and terminate the program
                           print("Program Completed!")
                           f.close()
                           os._exit(0)
                        count_commands = count_commands + 1
                        continue
                    else:
                        processToExecute.setBurst((int(processToExecute.getBurst()) - randomWaitTime)) #update burst time
                        InactiveQueue.put(processToExecute)
            count_commands = count_commands + 1


        while not InactiveQueue.empty(): #get all processes in the inactive queue into the active queue
            putToActive = InactiveQueue.get()
            ActiveQueue.put(putToActive)


if __name__ == "__main__":
    f = open("output.txt", 'w')
    sys.stdout = f
    clock = 0
    interval = 1
    expiry_count = 0
    maxSize=int(getCores())
    ActiveQueue = queue.Queue(maxsize=maxSize) #active queue with maxsize
    InactiveQueue = queue.Queue()
    #This returns an array of processes with their info (arrival time and burst time), and the number of cores and processes
    processes=read_processes()
    #This returns an array with a list of commands and their values
    listcommands = read_commands()
    t1 = threading.Thread(target=main) #main thread for the program/scheduler
    t1.start()
    t1.join()


