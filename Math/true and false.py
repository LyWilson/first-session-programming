p=[False,True]
print('p','   ','non(p)')
for i in p:
    print(i,not(i))

print('___________________')
q=[False,True]
for i in p:
    for j in q:
        print(i,j,i and j)

print('___________________')
r=[False,True]
for i in p:
    for j in q:
        for k in r:
            print(i,j,k,(not(i)and j)or k)
