st = "ramachandra"
m = {}
for i in st:
    m[i] = m.get(i,0) + 1
for i in m:
    if m[i] == 1:
        print(i,end=" ")
print()