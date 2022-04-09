array = [1,2,3,4,5,2,3,3]
array2 = []
for i in range(len(array)):
   k = i+1

   for j in range (k,len(array)):
        print(str(j))
        if array[i] == array[j] and array[i] not in array2:
            array2.append(array[i])




print(array2)