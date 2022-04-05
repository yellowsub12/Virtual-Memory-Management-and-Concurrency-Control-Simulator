cars = [2]
cars = ["Ford", "Das"]
carx = ["Toyota","BMW"]

#print(len(cars))
def isFull():
    for i in range(len(cars)):
     if cars[i] =='':
        print(str(i) + ' is empty')
        return i
    else:
        return -1

carz = []
carz.append(cars)
carz.append(carx)

#print(carz)
#print(carx)


#for x in cars:
#    print(x)
carz[0]=["Fordz","Daz"]
#print(carz)
#x = cars.index("")
#print(x)

print(isFull())
print(carz[0][2])

