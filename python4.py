from numpy import empty
n = 100
a = empty(n)
for i in range(1, n+1):
    a[i-1] = i

b = empty(n)
for i in range(1, n+1):
    b[i-1] = 2*i-1

a_sum = 0
for i in range(0, n):
    a_sum = a_sum + a[i]
a_average = a_sum/n

b_sum = 0
for i in range(0, n):
    b_sum = b_sum + b[i]
b_average = b_sum/n

numerator = 0
for i in range(0, n):
    numerator = numerator + (a[i]-a_average)*(b[i]-b_average)
covariance = numerator/n
print(covariance)
