from collections import defaultdict

d = defaultdict(int)
L = [1,2,3,1,2,3,4,1,2,3,4,1,1,2,2,3,3,3,3,4,4,5,6]

for i in L:
    d[i] += 1
print(d)
