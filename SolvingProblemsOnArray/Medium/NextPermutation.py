from typing import *
from itertools import permutations

def nextGreaterPermutation(A : List[int]) -> List[int]:
    # Write your code here.
    # n = len(A)
    # B = sorted(A)
    # li = list(permutations(B))
    # lastIndex = 0
    # for index,item in enumerate(li):
    #     if item == tuple(A):
    #         lastIndex = index
    # if lastIndex == len(li)-1:
    #     return li[0]
    # else:
    #     return li[lastIndex+1]

    n = len(A)
    breakPoint = None
    for i in range(n-2,-1,-1):
        if A[i] < A[i+1]:
            breakPoint = i
            break
    print("breakPoint : ",breakPoint)
    if breakPoint == None:
        return ReverseArray(A,0,n)
    else:
        j = findIndexOfSmallest(breakPoint,n-1,A,A[breakPoint])
        print("Smallest on right : ",A[j])
        A[i],A[j] = A[j],A[i]
        return ReverseArray(A,i+1,n)


def findIndexOfSmallest(low,high,arr,n):
    small = float("inf")
    ind = 0
    for i in range(low,high+1):
        if small >= arr[i] and n < arr[i]:
            small = arr[i]
            ind = i
    return ind

def ReverseArray(arr,low,high):
    n = high - low
    for i in range((n//2)):
        arr[low+i],arr[high-i-1] = arr[high-i-1],arr[low+i]
    return arr

if __name__ == "__main__":
    # print(nextGreaterPermutation([2,1,2,5,4,3,0,0]))
    print(nextGreaterPermutation([6,10, 8,13, 13 ]))


# 2 1 3 5 4 2 0 0  -- INput
# 2 1 3 0 0 2 4 5  -- OUTput

# output 
# 2 3 0 0 4 5 1