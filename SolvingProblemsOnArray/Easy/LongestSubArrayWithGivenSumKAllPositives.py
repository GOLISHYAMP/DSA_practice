def longestSubarrayWithSumK(a, k):
    n = len(a)
    if n == 0:
        return 0

    maxLen = 0
    currentSum = a[0]  # Initialize the current sum with the first element
    i, j = 0, 1

    while j <= n:
        if currentSum < k:
            if j < n:
                currentSum += a[j]
            j += 1
        elif currentSum == k:
            maxLen = max(maxLen, j - i)
            if j < n:
                currentSum += a[j]
            j += 1
        else:  # currentSum > k
            currentSum -= a[i]
            i += 1

    return maxLen

# Example usage:
a = [1, 2, 3, 4, 5]
k = 9
result = longestSubarrayWithSumK(a, k)
print(result)  # This should print 2, as [2, 3, 4] is the longest subarray with a sum of 9.
