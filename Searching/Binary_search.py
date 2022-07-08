def Binary_search(array,value):
    low = 0
    high = len(array)-1
    mid = (low+high)//2
    while not(array[mid]==value) and low<=high:
        mid = (low+high)//2
        if value > mid:
            low = mid + 1
            
        else:
            high = mid - 1
    if array[mid] == value:
        return mid
    else:
        return -1

arr =[3,4,5,6,7,8,9]
print(Binary_search(arr, 110))