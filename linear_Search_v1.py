# Problem Statement: "Given a sorted array of integers, and an integer x, find the first index of the array containing the number x, or return -1 in case the number doesn't appear in the array".

# Solution:

# Linear Search on a sorted Array
def no_brainer(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# a = [1,2,3,4,5,6,7,8,9,10]
# x = 10   
# output = no_brainer(a, x)
# print (output)

