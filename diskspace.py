vm_array = []

def vm(argument):
    vm = open("vm.txt", "w")
    vm_array.append(argument)
    x = vm_array[0]
    vm.write(str(x))

def print_vm():
    print(vm_array)

def read_disk():
    return vm_array

def remove(index):
    vm_array.pop(index)

def vm_replace(index, array):
    vm_array[index] = array





x = [('1', '2'), ('2', '7')]
vm(x)
print(read_disk())