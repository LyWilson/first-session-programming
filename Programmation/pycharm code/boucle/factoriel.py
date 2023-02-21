nb=int(input("saisir un nombre"))
fact = 1
for i in range(1,nb+1):
  fact = fact * i
  print(fact)
print (nb,'! = ',fact)