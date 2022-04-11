from argparse import Action
from hashlib import new
from itertools import count
from multiprocessing import process
from multiprocessing.connection import wait
from Process import Process
import queue
import threading
import os
from VirtualMemz import MemoryManager
from files import *
from diskspace import *
import random

def main():
    global clock
    clockthread = threading.Timer(interval, main).start()
    threads.append(clockthread)
    print("Clock is %d" % clock)
    clock = clock + 1000
    t2 = threading.Thread(target=scheduler())
    t2.start()
    threads.append(t2)
    t2.join()



def scheduler():
    global clock
    global count_processes
    global expiry_count
    expired_processes = []
    global processToExecute
    randomWaitTime = 0
    randomTimes = [100,200,300,400,500,600,700,800,900,1000]

    if count_processes < int(getNumProcesses()): 
            x = processes[count_processes] #initialize the new processes
            if x.getArrivalTime() <= clock : #current time of the clock:
                if ActiveQueue.full():
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    InactiveQueue.put(x)
                    count_processes = count_processes + 1
                else:
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    ActiveQueue.put(x)
                    count_processes = count_processes + 1

    for processToExecute in ActiveQueue.get():
        if count_commands == len(listcommands): #when all the commands are done, return to first command
            count_commands = 0
        if count_commands <= len(listcommands):
            line = listcommands[count_commands]
            x = line.split()
            if len(x) == 2: #in case we only have a variable id to use and no value to avoid array out of range
                MemoryManager(x[0], x[1], 0, clock, processToExecute)
                randomWaitTime = random.choice(randomTimes)
                if processToExecute.getBurst() < randomWaitTime:
                    processToExecute.setBurst(0)
                    print("Clock: " + str(clock) + ", " + str(processToExecute.getID()) + ": Finished")
                    expired_processes.append(processToExecute)
                else:
                    processToExecute.setBurst((processToExecute.getBurst() - randomWaitTime)) #update burst time
                    InactiveQueue.put(processToExecute)
                    expiry_count = expiry_count + 1
                    if expiry_count > (getNumProcesses() - 1): #check if all processes are done and terminate the program
                        print("Program Completed!")
                        f.close()
                        os._exit(0)
                    continue
            else:
                MemoryManager(x[0],x[1],x[2],clock,processToExecute)
                randomWaitTime  = random.choice(randomTimes)
                if processToExecute.getBurst() < randomWaitTime:
                    processToExecute.setBurst(0)
                    print("Clock: " + str(clock) + ", " + str(processToExecute.getID()) + ": Finished")
                    expired_processes.append(processToExecute)
                else:
                    processToExecute.setBurst((processToExecute.getBurst() - randomWaitTime)) #update burst time
                    InactiveQueue.put(processToExecute)
                    expiry_count = expiry_count + 1
                    if expiry_count > (getNumProcesses() - 1): #check if all processes are done and terminate the program
                        print("Program Completed!")
                        f.close()
                        os._exit(0)
                    continue
        count_commands = count_commands + 1
            if int(x.getArrivalTime()) <= clock : #current time of the clock:
                if ActiveQueue.full() is False :
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    ActiveQueue.put(x)
                    count_processes = count_processes + 1
                else:
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    InactiveQueue.put(x)
                    count_processes = count_processes + 1

    

 

    for putToActive in InactiveQueue.get(): #get all processes in the inactive queue in the active queue
        ActiveQueue.put(putToActive)


if __name__ == "__main__":
    f = open("output.txt", 'w')
    clock = 0
    clock = 1000
    interval = 1
    expiry_count = 0
    threads = []
    ActiveQueue = queue.Queue(maxsize=getCores())
    InactiveQueue = queue.Queue()
    count_processes = 0
    count_commands = 0
    array_of_active_processes = []
    #This returns an array of processes with their info (arrival time and burst time), and the number of cores and processes
    processes=read_processes()
    #This returns an array with a list of commands and their values
    listcommands = read_commands()
    t1 = threading.Thread(target=main) #main thread for the program/scheduler
    t1.start()
    threads.append(t1)
    t1.join()

