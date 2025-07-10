import random
x = random.uniform(0, 2)
y = random.uniform(0, 2)
print(x, y)

if x**2 + y**2 <= 1:
    print('circle')
else:
    print('not circle')
