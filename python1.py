from numpy import empty
n = 100
a = np.empty(n)
result = 0
for i in range(0, n, 1):
    result = result + a[i]
print(result)
