def pasc(x):
    pasc=[1]
    for i in range(len(x)-1):
        pasc.append(x[i]+x[i+1])
    pasc.append(1)
    return pasc

def pastri(ul):
    pex=[]
    lase=[]
    for i in range(ul):
        lase=pasc(lase)
        pex.append(lase)
    return pex

for i in pastri(10):
    print(i)
