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

# arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# for t in range(len(arr)-1):
#     if arr[t] == 0 and arr[t+1] != 0:
#         arr[t],arr[t+1] = arr[t+1],arr[t]
# print(arr)

# n = len(arr)
# for i in range(n):
#     if arr[i] == 0:
#         j = n-1
#         while(j>i):
#             if arr[j] != 0:
#                 arr[i],arr[j] = arr[j],arr[i]
#                 break
#             else:
#                 j -= 1
# print(arr)




def moveZeros(n,  a):
    j = -1
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    
    if j == -1:
        return a

    for i in range(j+1,n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j], arr[i]
            j += 1
    return a


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=' ')
print()




