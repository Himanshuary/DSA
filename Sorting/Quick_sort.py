from numpy import array


def Partition_logic(array,l,h):
    i = l
    j = h
    pivot = array[l]
    while i<j:
        while array[i] <= pivot:
            i= i + 1
        while array[j] >= pivot:
                j = j - 1
        if i<j:
            array[i], array[j] = array[j], array[i]
    pivot,array[j] = pivot ,array[j]
    return j

def Quick_sort(array,l,h):
    if l<h:
        pivot = Partition_logic(array,l,h)
        Quick_sort(l,pivot-1)
        Quick_sort(pivot+1,h)




arr = [4,6,2,5,7,9,1,3]
Quick_sort(array,0,len(arr))
print(array)