def longestConsecutiveSequence(arr):
    setArr = set()
    longest = 1
    cnt = 0
    for i in arr:
        setArr.add(i)

    for i in setArr:
        if i-1 not in setArr:
            cnt = 1
            x = i
            while x+1 in setArr:
                cnt += 1
                x += 1
            longest = max(longest,cnt)
    return longest

if __name__ == "__main__":
    arr=[100, 200, 1, 2, 3, 4]
    print(longestConsecutiveSequence(arr))