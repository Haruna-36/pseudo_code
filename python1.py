from numpy import empty
def sum_practice(n, a):
    result_sum = 0
    for i in range(0, n):
       result_sum = result_sum + a[i]
    return result_sum
