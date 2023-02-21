#9

#a)
p=[False,True]
for i in p:
    print(i and not(i))

print("-------------")
#b)
q=[False,True]
for a in p:
    for b in q:
        print((not(a))and(a and b))
print("-------------")
#c)
for c in p:
    for d in q:
        print((c and d))and (not((p and q)))
print("-------------")

#10
#a)
r=[False,True]
for e in p:
    for f in q:
        for g in r:
            print(e and (not((e or f) or g)))
print("-------------")

#b)
for e in p:
    for f in q:
        for g in r:
            print((e and not(f))and not(f and not(e)))
print("-------------")
#c)
for e in p:
    for f in q:
        for g in r:
            print(((e and not(f))== f) and not(e))
print("-------------")
#d)
for e in p:
    for f in q:
        for g in r:
            print(e and not(f and not(f and not(e))))
