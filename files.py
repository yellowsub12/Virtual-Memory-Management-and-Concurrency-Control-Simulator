from os import read
from Process import Process


def read_processes():
    open_file = open("processes.txt" , "r")
    global number_cores 
    number_cores = open_file.readline()
    global number_processes 
    number_processes = open_file.readline()
    count = 0
    tempSort=1000000000000
    tempArraySorting = []
    lines = []
    return_array = []
    for line in open_file:
        lines.append(line)
    open_file.close()
    temp_array = lines
    for j in temp_array:
        j = temp_array[count]
        x = j.split()
        pid = "P" + str(count + 1)
        arrival_time = x[0]
        burst = x[1]
        process = Process(pid, arrival_time,burst)
        return_array.append(process)
        count = 1 + count
        tempSort=return_array[0]
    for i in range(0,len(return_array)):
        k = i +1
        for j in range(k,len(return_array)):
            if return_array[j].getArrivalTime() < tempSort.getArrivalTime():
                tempSort = return_array[j]
                return_array[i] = return_array[j]
                return_array[j] = tempSort

           

    return return_array

def read_memconfig():
    open_file = open("memconfig.txt", "r")
    number_pages = open_file.readline()
    k_value = open_file.readline()
    timeout = open_file.readline()
    return_array = []
    return_array.append(number_pages)
    return_array.append(k_value)
    return_array.append(timeout)
    return return_array

def read_commands():
    open_file = open("commands.txt", "r")
    lines = []
    for line in open_file:
        lines.append(line)
    open_file.close()
    return lines

def separate_commands(lines, counter, commands):
    i = lines[counter]
    x = i.split()
    commands.append(x[0])
    commands.append(x[1])
    commands.append(x[2])
    counter = counter + 1
    print(commands)

def getCores():
    return number_cores

def getNumProcesses():
    return number_processes

counter = 0
commands = []

