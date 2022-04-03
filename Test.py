cars = [4]
cars = ["Ford", "Das", "BMW", "Dracula"]

#print(len(cars))
def isFull():
    for i in range(len(cars)):
     if cars[i] =='':
        print(str(i) + ' is empty')
        return i
    else:
        return -1
    

#for x in cars:
#    print(x)

#x = cars.index("")
#print(x)

print(isFull())