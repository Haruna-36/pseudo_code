import python1

from numpy import empty
n = 100
a = empty(n)
for j in range(1, n+1):
    a[j-1] = j
average = 0
average = python1.sum_practice(n, a)/100
print(average)
