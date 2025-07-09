from numpy import empty
n = 100
a = empty(n)
for i in range(1, n+1):
    a[i-1] = i

for i in range(0, n-1):
    if a[i] > a[i+1]:
        a[i+1] = a[i]

max_value = a[n-1]
print(max_value)
