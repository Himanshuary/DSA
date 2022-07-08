def Linear_search(list,value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1


arr = [1,3,2,5,4,9,7,6,8]
print(Linear_search(arr,70))