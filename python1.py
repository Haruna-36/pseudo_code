from numpy import empty
n = 100
a = empty(n)
for j in range(1, n+1):
    a[j-1] = j
result1 = 0
for i in range(0, n):
    result1 = result1 + a[i]
print(result1)
