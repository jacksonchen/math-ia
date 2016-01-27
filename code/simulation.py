import random
import time

points = 100000
cumSum = 0
n = points

start = time.time()
for j in range(1000):
    pointsOut = 0
    pointsIn = 0
    x = [random.random()*6 for i in xrange(n)]
    y = [random.random()*6 for i in xrange(n)]
    for i in range(n):
        if (y[i] < (-(0.5*x[i]-2.5) ** 2 + 5) and y[i] > (x[i]-3) ** 2):
            pointsIn += 1
    cumSum += pointsIn

f = open('result.txt', 'w')
f.write(str(cumSum/1000))
f.close()
end = time.time()
print end - start
