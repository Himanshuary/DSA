# Find the missing number in sequeation

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30]

def findmissing(list, n):
    sum1 = (n*(n+1))/2
    sum2 = sum(list)
    print("Missing number is: ", sum1-sum2)

findmissing(mylist, 30)