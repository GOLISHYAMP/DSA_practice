# def count_num(arr,n):
#     co = 0
#     for i in arr:
#         if i == n:
#             co += 1
#     if co == 1:
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     arr = [1,1,2,4,3,4,3]
#     for i in arr:
#         if count_num(arr,i):
#             print(i)
#             break
    


# if __name__ == "__main__":
# arr = [1,1,2,4,3,4,3]
# dic = {}
# for i in arr:
#     dic[i] = dic.get(i,0) + 1
# for i in dic:
#     if dic[i] == 1:
#         print(i)
#         break    

def find_single(arr):
    xor = 0
    for i in arr:
        xor ^= i
    return xor
if __name__ == "__main__":
    arr = [1,1,2,4,3,4,3,3,2]
    print(find_single(arr))