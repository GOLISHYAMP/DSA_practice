def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    # 10 20 -30 40 -50 60
    # MAX_SUM = 0
    # for i in range(1,n+1):
    #     # print(arr[0:i])
    #     s = sum(arr[0:i])
    #     if MAX_SUM < s:
    #         MAX_SUM = s
    # for i in range(n-1,-1,-1):
    #     # print(arr[i:])
    #     s = sum(arr[i:])
    #     if MAX_SUM < s:
    #         MAX_SUM = s
    # return MAX_SUM

    # maxi = -sys.maxsize-1 # maximum sum
    maxi = 0
    sum = 0
    start = 0
    ansstart = -1
    ansend = -1
    for i in range(n):
        if sum == 0:
            start = i
        sum += arr[i]

        if sum > maxi:
            maxi = sum
            ansstart = start
            ansend = i

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0
            
    print(arr[ansstart:ansend+1])
    return maxi

if __name__ == "__main__":
    print(maxSubarraySum([1, 2, 7, -4, 3, 2, -10, 9, 1],9))