# from itertools import product
# l = list(product(range(30,50,5), range(1,10,3)))

import random
import time

points = 1000
cumSum = 0
n = 50

start = time.time()
for j in range(1000):
    pointsOut = 0
    pointsIn = 0
    x = [random.random()*4 for i in xrange(n)]
    y = [random.random()*4 for i in xrange(n)]
    for i in range(n):
        if ((x[i] - 2) ** 2 + (y[i] - 2) ** 2 <= 4):
            pointsIn += 1
    cumSum += pointsIn

f = open('result.txt', 'w')
f.write(str(cumSum/1000))
f.close()
end = time.time()
print end - start
