# arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# temp = []
# for i in arr:
#     if i != 0:
#         temp.append(i)
# n = len(temp)
# for i in range(len(arr)):
#     if i >= n:
#         arr[i] = 0
#     else:
#         arr[i] = temp[i]
# print(arr)

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# for t in range(len(arr)-1):
#     if arr[t] == 0 and arr[t+1] != 0:
#         arr[t],arr[t+1] = arr[t+1],arr[t]
# print(arr)
i = 0
j = 0
n = len(arr)
while(i< n and j < n):
    while(arr[i] != 0):
        i += 1
        j = i + 1


