n = 6
arr = [2,13,1,52,20,9]
# [2,13,1,52,20,9]

for i in range(n):
    k = i
    while(arr[k]<arr[k-1] and k != 0):
        arr[k],arr[k-1] = arr[k-1],arr[k]
        k -= 1
print(arr)

# for i in range(1,n):
#     # print("i = ",i)
#     for k in range(i,0,-1):
#         if arr[k]<arr[k-1]:
#             arr[k],arr[k-1] = arr[k-1],arr[k]
#         # print(k)
# print(arr)