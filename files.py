from os import read
from Process import Process


def read_processes():
    open_file = open("processes.txt" , "r")
    number_cores = open_file.readline()
    number_processes = open_file.readline()
    count = 0
    lines = []
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
        process.print()
        count = 1 + count
    return number_cores

def read_memconfig():
    open_file = open("memconfig.txt", "r")
    number_pages = open_file.readline()
    k_value = open_file.readline()
    timeout = open_file.readline()
    return_array = []
    return_array.append(number_pages)
    return_array.append(k_value)
    return_array.append(timeout)
    print(return_array)
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

counter = 0
commands = []
temp = read_commands()
separate_commands(temp, counter, commands)
separate_commands(temp, counter, commands)