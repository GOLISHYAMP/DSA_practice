def checkPrime(n):
    if n == 1 or n == 2:
        return True
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    j = 0
    n = int(input())
    for i in range(1,n+1):
        if checkPrime(i):
            # print(i)
            if j == 1:
                j = 0
                print(i)
            else:
                j = 1
    
