#question 1
x=3
y=2**x
x=2*x+1
y=y-2*x
print("question 1 :",x,y)

#question 2
x=2
y=5
z=9
w=x
x=y
y=z
z=w
print("question 2 :",x,y,z)

#question 3
from math import*
a=2 
b=sqrt(a)
print("question 3 :",a,b)

#question 4
print("question 4:")
A=[1,0,0,1,1,1,0,1]
print(A)
B=[0,0,0,0,0,0,0,0]
for i in range(8):
    B[i]=1-A[i]
print(B)

#question 5

#1)
print("question 5 (1):")
A=[1,0,0,1,1,1,0,1] #donne les valeurs a A
print(A[0]) #affiche la valeur de premier terme
print(A[2]) #afficher la valuer de troisieme terme
for i in range(8): #debuter un boucle
	print(A[i]) #affiche la valeur de A dans la boucle
a= A[0]*2**7+ A[1]*2**6+ A[2]*2**5+ A[3]*2**4+ A[4]*2**3+ A[5]*2**2+ A[6]*2**1+ A[7]*2**0 #operation arithmétique qui donne une valeur a "a"
print(a) #affiche la valuer de "a"

#2)
print("question 5 (2):")
A=[1,0,0,1,1,1,0,1] #donne les valeurs de A
B=[0,0,0,0,0,0,0,0] #donne les valuers de B
for i in range(8): #debuter une boucle
    B[i]=2**(7-i)  #l'operation dans la boucle et qui donne les valeurs de B
print(A) #affiche les valeurs de A
print(B) #affiche les valeurs de b
a=0 #donne une valeur a a
for i in range(8):  #debuter une boucle
    a=a+A[i]*B[i] #l'operation dans la boucle et qui donne les valeurs de a
print('le nombre entier represente par A est',a) #affiche la valeur de a suite a la boucle
    #1*128
    #0*64
    #0*32
    #1*16
    #1*8
    #1*4
    #0*2
    #1*1

#question 6
print("qestion 6 (1):")
A=[] #donne la valeur de A  
print(A) #affiche la valeur de A
A=[1]+A #ajoute 1 dans la liste de A
print(A) #affiche la valeur de A
A=[0]+A #ajoute 0 dans la liste de A
print(A) #affiche la valeur de A
A=[0]+A #ajoute 0 dans la liste de A
print(A) #affiche la valeur de A
A=[1]+A #ajoute 1 dans la liste de A
print(A) #affiche la valeur de A
 
print("qestion 6 (1):")
a=137 #donne une valeur a a
b=a #donne la valeur de a à b
A=[] #definie la valeur de A
for i in range(8): #debuter une boucle
    reste=a%2 #operation arithmétique dans la boucle
    print("le reste est",reste) #affiche le reste de l'opération
    a=a//2 #faire une opération arithmetique pour trouver la division de l'entier par 2
    print("Le quotient est",a)#affiche la variable a
    A=[reste]+A #operation arithmétique qu addition le reste avec A
    print(A)#affiche la valeur de A
print("le nombre",b,"est represente par l’octet",A)#affiche la valeur de b et A suite a la boucle

