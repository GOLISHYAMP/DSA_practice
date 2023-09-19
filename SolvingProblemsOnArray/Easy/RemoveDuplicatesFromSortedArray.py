# def check(arr,n):
#     for i in range(len(arr)):
#         if arr[i] == n:
#             return True
#     arr.append(n)
#     return False

# def removeDuplicates(arr,n):
#     # val = 0
#     temp = []
#     for i in arr:
#         check(temp,i)
#     return len(temp)

# def removeDuplicates(arr,n):
#     # val = 0
#     temp = {}
#     for i in arr:
#         if i in temp.keys():
#             temp[i] += 1
#         else:
#             temp[i] = 1
#     return len(temp)

# Most Efficient way of code O(n)
def removeDuplicates(arr,n):
    temp = 0
    prev = arr[0]
    temp = 1
    for i in range(1,n):
        if arr[i] != prev:
            temp += 1
            prev = arr[i]
    return temp

arr = [1,2 ,2 ,3 ,3 ,3 ,4 ,4 ,5 ,5]
print(removeDuplicates(arr,len(arr)))