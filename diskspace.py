vm_array = []

def vm(argument):
    vm = open("vm.txt", "w")
    vm_array.append(argument)
    x = vm_array[0]
    vm.write(str(x))

def print_vm():
    print(vm_array)


x = [('1', '2'), ('2', '7')]
vm(x)
print_vm()