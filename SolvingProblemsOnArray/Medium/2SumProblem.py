def read(n, book, target):
    # Write your code here.
    # for i in range(len(book)):
    #     for j in range(i,len(book)):
    #         if (book[i]+book[j]) == target:
    #             return "YES"
    # return "NO"

    i = 0
    while(i<n):
        j = i+1
        find = target - book[i]
        while(j<n):
            if book[j] == find:
                return "YES"
            j+=1
        i += 1
    return "NO"

if __name__ == "__main__":
    print(read(5,[4, 1, 2, 3, 1],5))