# Creating a array using python
from array import*

arr1 = ('i', [10,20,30,40,50])
print(arr1)

# By user input
arr2 = array("i",[])
n = int(input("Enter length an array: "))
for i in range(n):
    v = int(input("Enter value of an array:"))
    arr2.append(v)
    
    
print(arr2)