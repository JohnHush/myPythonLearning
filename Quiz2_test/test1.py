import random


g1 =0 
g2 =0
mean =100.
stdDev1 = 0.
stdDev2 = 20.

for i in range(1000):
    g1 += random.gauss(mean, stdDev1 )
    g2 += random.gauss( mean, stdDev2)
print g1
print g2
