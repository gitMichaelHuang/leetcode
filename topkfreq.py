from collections import defaultdict

nums = [1,2,2,2,3,3,3,3,4,4]
k = 2

d = defaultdict(int)
for i in nums:
    d[i] += 1

l = []
for key, val in d.items():
    l.append([val,key])
print(l)
l.sort(reverse=True)
print(l)

res = []
for i in range(k):
    res.append(l[i][1])

print(res)
