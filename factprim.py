ul =   105000
term = 10001

prim =[]
for n in range(1,ul+1):
    fact = []
    m=n
    for i in range(2,n):
        if n%i==0:
            fact.append(i)
    if len(fact) == 0:
        prim.append(m)
print(len(prim))
print(prim[term-1])

