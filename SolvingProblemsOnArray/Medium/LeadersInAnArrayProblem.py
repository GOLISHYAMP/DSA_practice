def superiorElements(a):
    # Write your code here.
    n = len(a)
    li = []
    large = float("-inf")
    for i in range(n-1,-1,-1):
        if large < a[i]:
            # print("large : ",large)
            large = a[i]
            li.append(a[i])
    return li

if __name__ == "__main__":
    print(superiorElements([1, 2, 2, 1]))