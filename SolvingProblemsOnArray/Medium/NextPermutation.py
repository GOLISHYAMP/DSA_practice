from typing import *
from itertools import permutations

def nextGreaterPermutation(A : List[int]) -> List[int]:
    # Write your code here.
    n = len(A)
    B = sorted(A)
    li = list(permutations(B))
    # print(li)
    # print(tuple(A))
    # print(li.index(tuple(A)))
    lastIndex = 0
    for index,item in enumerate(li):
        if item == tuple(A):
            lastIndex = index
    if lastIndex == len(li)-1:
        return li[0]
    else:
        return li[li.index(tuple(A))+1]
    # return li

if __name__ == "__main__":
    print(nextGreaterPermutation([6, 10, 8, 13, 13]))