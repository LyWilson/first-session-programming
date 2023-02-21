#question

import statistics
from math import*

L = [255,255,255,255,255,255,255,150,150,150,150,150,150,150,0,0,0,0,0,128,128,128,128,128,128,128,100,200,200,200,200,200,50,50,50,50]


#a)mode de la distribution

print(statistics.mode(L))

#b)mediane

print(statistics.median(L))

#c)moyenne et ecart type

print(statistics.mean(L))
print(statistics.stdev(L))
