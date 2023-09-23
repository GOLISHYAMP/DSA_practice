def uni(a,b):
    i,j = 0,0
    m = len(a)
    n = len(b)
    temp = []
    while((i < m) and (j < n)):
        if a[i] <= b[j]:
            if len(temp) == 0 or temp[-1] != a[i]:
                temp.append(a[i])
            i += 1
        else:
            if len(temp) == 0 or temp[-1] != b[j]:
                temp.append(b[j])
            j += 1
    while (i < m):
        if temp[-1] != a[i]:
            temp.append(a[i])
        i += 1
    while (j < n):
        if temp[-1] != b[j]:
            temp.append(b[j])
        j += 1
    return temp


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 6]
    arr2 = [2, 3, 5]
    print(uni(arr1,arr2))