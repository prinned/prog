import math

def f(x):
    f=0
    for i in range(len(str(x))):
        f += int(str(x)[i])**2
    return f

bg=[]
for i in range(1,100):
    if math.sqrt(f(i))%1==0:
        bg.append([i,f(i)])

for i in bg:
    print(i)
