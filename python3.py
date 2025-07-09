from numpy import empty
n = 100
a = empty(n)
for i in range(1, n+1):
    a[i-1] = i

result_sum = 0
for i in range(0, n):
    result_sum = result_sum + a[i]
result_average = result_sum/n

numerator = 0
for i in range(0, n):
    numerator = numerator +  (a[i] - result_average)**2
variance = numerator/n
print(variance)
