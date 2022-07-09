def Bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j] #swap element
    
    return array

arr = [-2,45,0,11,-9]
print(Bubble_sort(arr))