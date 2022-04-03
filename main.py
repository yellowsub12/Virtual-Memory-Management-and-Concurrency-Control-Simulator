from hashlib import new
from multiprocessing.connection import wait
from Process import Process
import queue
import sys
import threading
import os
import math

def read_file(): #read the file line by line and store the lines in an array
    open_file = open("input.txt", "r")
    lines = []
    for line in open_file:
        lines.append(line)
    open_file.close()
    return lines

def create_processes(array): #create an array of processes and sort the process with their arrival time.
    global nb_processes 
    nb_processes = int(array[0])
    new_array = array[1:]
    return_array = []
    count = 0
    previous_time = 0
    temp = 0

    for i in new_array:
        i = new_array[count]
        x = i.split()
        pid = x[0]
        arr_time = int(x[1])
        burst = int(x[2])
        priority = x[3]
        process = Process(pid,arr_time,burst,priority) #creation of the object
        if arr_time < previous_time and 1 < count:
            temp = return_array.pop(count-1)
            return_array.insert(count - 1, process)
            return_array.append(temp)
        else:
            return_array.append(process)
        previous_time = arr_time
        count = count + 1
        if count == len(new_array):
            break
    return return_array

def updates(process, waiting_time): #the function that will update the priority of the processes after two execution
    old_priority = process.getPriority() 
    bonus = math.floor((10*waiting_time)/(clock - process.getArrivalTime()))
    new_priority = max(100,min((int(old_priority) - int(bonus) + 5), 139))
    return new_priority


def waiting_times(process, clock): #this function calculates the total waiting time of the process since it started its first execution.
    if process.getNbUpdate() == 0: #if the process updates for the first time
        temp = clock - process.getLastExecution() - process.getArrivalTime()
        process.setWaiting(temp)
        process.setNbUpdate(1)
    else: #else
        process.setWaiting((clock - process.getLastExecution())) 
    return process.getWaiting()



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


def scheduler():
    global flag1 #make global variables of the program for the flags and clock
    global flag2
    global clock
    global count_processes
    global expiry_count

    expired_processes = []


    while True:

        #this first if statement is a buffer. Its purpuse is to hold the next process to be put in a queue. The variable x holds the first process in the array that was returned
        #by the create_process function. The variable x will hold the process until the arrival time of the process matchtes that of the clock.
        #If the previous contition is true then it will check which queue is the inactive one and put it inside.

        if count_processes < nb_processes: 
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

        #The next segment of clock checks if the active queue is empty and switched the flags if that is the case.

        if flag1 == True and queue1.empty():
                flag1 = False
                flag2 = True
        elif flag2 == True and queue2.empty():
                flag1 = True
                flag2 = False
    
    
        #this algorithm executes the process, starts the threads and terminates the process if they are at the end.
        if flag1 == True:
            execution = queue1.get()
            if execution.getNumberExecution() < 1: #check if the process never executed before to start its thread
                execution.start() #start the thread
            execution.join() #join the thread
            print("Time " + str(clock) + ", " + str(execution.getID()) + ", Started, Granted " + str(execution.time_slot()))
            wait_time = waiting_times(execution, clock) #calculate the waiting time
            if execution.time_slot() < execution.getBurst(): #check for process termination
                clock = clock + execution.time_slot() #execute time slot
                execution.setLastExecution(clock)   #record the completion time for future waiting time calculations
                temp = (execution.getBurst() - execution.time_slot())
                execution.setBurst(temp) #set the remaining time for the process
                execution.setNumberExecution() #update the number of times this process has executed to check is priority needs to be updated
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Paused")
                if execution.getNumberExecution() % 2 == 0: #checks if the process needs a priority update
                    execution.setPriority(updates(execution, wait_time)) #update the priority
                    print("Time " + str(clock) + ", " + str(execution.getID()) + ", Priority updated to " +  str(execution.getPriority()))
                queue2.put(execution) #put the process back in the inactive queue
            else: #process enters this else if it is due for termination
                clock = clock + execution.getBurst() #update the clock for execution
                execution.setBurst(0) # process is finished
                expired_processes.append(execution) #put the process in a discard array
                expiry_count = expiry_count +1 #counts the number of process terminated for the termination of the whole program
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Finished")
                if expiry_count > (nb_processes - 1): #check if all processes are done and terminate the program
                    print("Program Completed!")
                    f.close()
                    os._exit(0)
                continue
        #the else statement below executes the same functions as the if it is liked with
        else:
            execution = queue2.get()
            if execution.getNumberExecution() < 1:
                execution.start()
            execution.join()
            print("Time " + str(clock) + ", " + str(execution.getID()) + ", Started, Granted " + str(execution.time_slot()))
            wait_time = waiting_times(execution, clock)
            if execution.time_slot() < execution.getBurst():
                clock = clock + execution.time_slot()
                execution.setLastExecution(clock)
                temp = (execution.getBurst() - execution.time_slot())
                execution.setBurst(temp)
                execution.setNumberExecution() #update the number of times this process has executed in a row
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Paused")
                if execution.getNumberExecution() % 2 == 0:
                    execution.setPriority(updates(execution, wait_time))
                    print("Time " + str(clock) + ", " + str(execution.getID()) + ", Priority updated to " +  str(execution.getPriority()))
                queue1.put(execution)
            else:
                clock = clock + execution.getBurst()
                execution.setBurst(0) # process is finished
                expired_processes.append(execution)
                expiry_count = expiry_count +1
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Finished")
                if expiry_count > (nb_processes - 1):
                    print("Program Completed!")
                    f.close()
                    os._exit(0)
                continue

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
    pass1 = read_file()
    processes = create_processes(pass1)
    count_processes = 0
    t1 = threading.Thread(target=main) #main thread for the program/scheduler
    t1.start()
    threads.append(t1)
    t1.join()
