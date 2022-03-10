# Write a program to find all pair of integers whose sum of equal to a given number

def findpair(nums, traget):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i]+nums[j] == traget:
                print(i, j)
            

mylist = [1,2,3,2,3,4,5,6]
findpair(mylist, 4)