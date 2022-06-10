from array import *

arr1 = array('i', [10,20,30,40,50])

# Traverse an array
for i in arr1:
    print(i)


# Access individual elements through indexs
print("Step--2\n")
print("Array 0 index value is: ", arr1[0])

# Extend python array using extend() method
print("step--3\n")
arr2 = array('i', [60,70,80,90,100])
arr1.extend(arr2)
print(arr1)

# Add iteam from list into an array using fromlist() method
print('Step--4\n')
list1 = [110,120,130,140]
arr1.fromlist(list1)
print(arr1)

# Remove any element in array using remove() method
print("Step--5\n")
arr1.remove(140)
print(arr1)

# Remove any element in array using pop() method
print("Step--6\n")
arr1.pop()
print(arr1)

# Fetch any element through its index using index method
print("Step--7\n")
print("120 value index number is: ",arr1.index(120))

# Reverse an array using reverse() method
print("Step--8\n")
arr1.reverse()
print(arr1)

# Get array buffer information through buffer_info() method
print("Step--9\n")
print(arr1.buffer_info())

# Check the number of occurences of an element using cout() method
print("Step--10\n")
print(arr1.count(20))

# covert array into python list using tolist() method
print("Step--11\n")
arr3 = arr1
print(arr1.tolist())