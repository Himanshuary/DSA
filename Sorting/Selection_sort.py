def Selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if array[min_index] > array[j]:
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]
    return array
arr = [20,12,10,15,2]
print(Selection_sort(arr))