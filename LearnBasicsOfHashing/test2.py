v = [1, 2, 3, 1, 1, 4]
hash = {}
n = len(v)
for i in range(1,n+1):
    hash[i] = 0
for i in v:
    hash[i] += 1
maxVal = max(hash.values())
print(maxVal)
print(hash.values())
minVal = list(map(lambda x : x>0, hash.values()))
mv = list(map(hash.values(),minVal))
print(mv)
final = [0,0]
for i in range(1,len(hash)+1):
    if hash[i] == maxVal and final[0] == 0:
        final[0] = hash[i]
    if hash[i] == minVal and final[1] == 0:
        final[1] = hash[i]
print(final)