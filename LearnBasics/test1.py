# arr = [11,17, 3, 5, 7,8,1,2]   out : [17, 8, 2]

arr = [13, 12, 3, 5, 7, 1]
temp = []

while len(arr) > 0:
    m = max(arr)
    temp.append(m)

    ind = arr.index(m)
    arr = arr[ind + 1:]
    # print(arr)

print(temp)