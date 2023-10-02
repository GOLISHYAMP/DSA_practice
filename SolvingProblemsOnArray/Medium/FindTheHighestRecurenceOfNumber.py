def findRecurence(num,n):
    count = 0
    while(num > 0):
        temp = num % 10
        if temp == n:
            count += 1
        num = int(num / 10)
    return count


if __name__ == "__main__":
    arr = [12,22,22,121,34,54,26,725]
    n = 2
    maxi = 0
    number = 0
    for i in arr:
        temp = findRecurence(i,n)
        if maxi < temp:
            maxi = temp
            number = i
    print(number)

