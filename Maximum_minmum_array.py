from array import *
arr = array("i",[])
n =int(input("Enter lenght of array: "))
for i in range(n):
    x = int(input("Enter value of array: "))
    arr.append(x)

print(arr)


# maximum
max = 0
for i in arr:
    if max < i:
        max = i

print("Maximum number in array is: ",max)

# Minimum
mini = arr[0]
for i in arr:
    if mini >= i:
        mini = i
        
print("Minimum number in array is: ",mini)
