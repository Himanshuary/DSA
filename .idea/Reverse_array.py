from array import *
# Iterative python program to reverse an array
list1 = [1,2,3,4,5,6]
print("List is: ", list1)
def reverselist(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start = start + 1
        end = end - 1
    return list


print("Reverse list is: ", reverselist(list1, 0, 5))


# Recursive python program to reverse an array

list2 = [7,8,9,10,11,12]
print("List is: ", list2)
def reverselist(list, start, end):
    while start >= end:
        return
    list[start], list[end] = list[end], list[start]
    reverselist(list, start+1, end-1)

reverselist(list2, 0, 5)
print("reverse list is: ", list2)

# reverse array
arr = array('i', [10,20,30,40,50])
print("Array is: ", arr)
arr.reverse()
print("Reverse array is: ",arr)