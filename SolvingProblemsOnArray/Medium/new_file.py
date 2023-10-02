# import FindTheHighestRecurenceOfNumber as fh

# print(fh.findRecurence(121,1))

arr = [1,2,3,4,5,6,7,8,9]
print("arr : ",arr)
# print(reversed(arr))
# arr = arr[::-1]
# print()
# print(arr)
# n = len(arr)
# for i in range((n//2)):
#     arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
# print(arr)


arr = [1,2,3,4,5,6,7,8,9]
print("arr : ",arr)

def ReverseArray(arr,low,high):
    n = high - low
    for i in range((n//2)):
        arr[low+i],arr[high-i-1] = arr[high-i-1],arr[low+i]
    return arr
print(ReverseArray(arr,3,8))