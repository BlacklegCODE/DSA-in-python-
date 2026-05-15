from collections import defaultdict

d = defaultdict(list)

for i in range(10):
  d[i].append(i)

print(d)
