 while True:

        #this first if statement is a buffer. Its purpuse is to hold the next process to be put in a queue. The variable x holds the first process in the array that was returned
        #by the create_process function. The variable x will hold the process until the arrival time of the process matchtes that of the clock.
        #If the previous contition is true then it will check which queue is the inactive one and put it inside.

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
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Paused")
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
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Paused")
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