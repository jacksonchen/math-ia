# from itertools import product
# l = list(product(range(30,50,5), range(1,10,3)))

import random
pointsIn = 0
x = [random.random()*4 for i in xrange(1000)]
y = [random.random()*4 for i in xrange(1000)]
for i in range(1000):
    if ((x[i] - 2) ** 2 + (y[i] - 2) ** 2 <= 4):
        print [x[i], y[i]]
        pointsIn += 1
# print(pointsIn)
