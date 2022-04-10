from hashlib import new
from multiprocessing.connection import wait
from Process import Process
import queue
import threading
import os
from files import *
from diskspace import *

#This returns an array of processes with their info (arrival time and burst time), and the number of cores and processes

#This returns an array with the values of number of pages [0], K value [1] and time-out [2]
read_memconfig()
#This returns an array with a list of commands and their values
read_commands()






def scheduler():
    global flag1 #make global variables of the program for the flags and clock
    global flag2
    global clock
    global count_processes
    global expiry_count
    expired_processes = []

    if count_processes < getNumProcesses(): 
            x = processes[count_processes] #initialize the new processes
            if x.getArrivalTime() <= clock : #current time of the clock:
                if flag1 == True:
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    queue2.put(x)
                    count_processes = count_processes + 1
                else:
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    queue1.put(x)
                    count_processes = count_processes + 1


   


def main():
    global clock
    clockthread = threading.Timer(interval, main).start()
    threads.append(clockthread)
    print("Clock is %d" % clock)
    clock = clock + 1000

    t2 = threading.Thread(target=scheduler)
    t2.start()
    threads.append(t2)
    t2.join()

if __name__ == "__main__":
    f = open("output.txt", 'w')
    flag1 = True     #queue1 flag
    flag2 = False #queue2 flag
    clock = 0
    interval = 1
    expiry_count = 0
    threads = []
    queue1 = queue.Queue()
    queue2 = queue.Queue()
    count_processes = 0

    #This returns an array of processes with their info (arrival time and burst time), and the number of cores and processes
    processes=read_processes()

    #This returns an array with the values of number of pages [0], K value [1] and time-out [2]
    read_memconfig()
    #This returns an array with a list of commands and their values
    listcommands = read_commands()

    t1 = threading.Thread(target=main) #main thread for the program/scheduler
    t1.start()
    threads.append(t1)
    t1.join()
