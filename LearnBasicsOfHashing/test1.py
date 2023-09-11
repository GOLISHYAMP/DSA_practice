# from typing import *

# def countFrequency(n: int, m: int, edges: List[List[int]]):
n = 6
m = 9
edges = [1, 3, 1, 9, 2, 7]
hash = {}
for i in range(1,m+1):
    hash[i] = 0
print(hash)
for i in range(0,n):
    hash[edges[i]] += 1
li = []
for i in range(1,n+1):
    li.append(hash[i])
print(li)
# return edges