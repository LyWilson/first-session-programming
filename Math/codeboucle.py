#numero 1
#a)
for i in range(101):
    print(i**3)

#b)
for a in range(10,21):
    print(a**4)

#c)
from math import*

for s in list(range(0,101,5)):
    print(sqrt(s))

#numero 2
for b in range(1,11):
    print(2**b)


#numero 3
x=i/100
for i in range(101):
    x=i/100
    y=(x**3)-(x**2)-(x/4)+1
    print("x =",x,"y =",y)
#verification manuel reponse: x=1 Y=3/4 ou 0.75

#numero 4
for r in range(101):
    V=(4/3)*(3.1415)*(r**3)
    print("R =",r,"V =",V)
