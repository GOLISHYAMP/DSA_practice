def FindTheMaximumSumOfSubArray(arr,n):
    sum = 0
    maxi = 0
    ansStart = 0
    ansEnd = 0
    start = 0
    for i in range(n):
        sum += arr[i]
        if maxi < sum:
            maxi = sum
            ansStart = start
            ansEnd = i
        if sum < 0:
            sum = 0
            start = i
    print(arr[ansStart:ansEnd+1])
    return maxi
        


if __name__ == "__main__":
    print(FindTheMaximumSumOfSubArray([1, 2, 7, -4, 3, 2, -10, 9, 1],9))