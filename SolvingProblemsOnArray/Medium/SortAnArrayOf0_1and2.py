from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):
	# i,j,k = 0,0,0
	# for t in arr:
	# 	if t == 0:
	# 		i += 1
	# 	elif t == 1:
	# 		j += 1
	# 	else:
	# 		k += 1
	# # print(i,j,k)
	# p = 0
	# for _ in range(i):
	# 	arr[p] = 0
	# 	p += 1
	# for _ in range(j):
	# 	arr[p] = 1
	# 	p += 1
	# for _ in range(k):
	# 	arr[p] = 2
	# 	p += 1
    low = 0
    mid = 0
    high = n-1
    while(mid <= high):
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1
	
		
			
if __name__ == "__main__":
	arr = [2, 2, 2, 2, 0, 0, 1, 0]
	n = 8
	sortArray(arr,n)
	print(arr)
	