from asyncio.windows_events import NULL
from contextlib import nullcontext
from hashlib import new
from multiprocessing.connection import wait
import queue
import sys
import threading
import os
import math


def pageCreation(array):
    global nb_pages 
    nb_pages = int(array[0])
    new_array = array[1:]
    return_array = []
    count = 0
    previous_time = 0
    temp = 0


def Store(Page)
    if memoryPageAvailable != -1 :
        mainMemory.append(Page)


def memoryPageAvailable(memQueue): #Add Page to memory 
    #Determine if there's free space
    if memQueue.full():
        print("FULL")
        return -1

def mainMemoryPageAdd(pages):
    if memoryPageAvailable(memQueue) != -1 :
        print("We can add shit here")
        memQueue.put(pages)


def main():
    global clock

if __name__ == "__main__":
    t1 = threading.Thread(target=main) 
    pages = [3] 
    mainMemory = [len(pages)]
    diskMemory = [] 
    totalMemory = []



    memoryPageAvailable()
    mainMemoryPageAdd()
    t1.start()
    t1.join()