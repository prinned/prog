def check(x):
    xl=[]
    for i in str(x):
        xl.append(int(i))

    for i in range(len(xl)-1):
        if xl[i]+xl[i+1]+xl[i+2] > 9:
            return False
            break
        elif i+3 >=len(xl)-1:
            return True
            break

bg=0
for i in range(100000,1000000):
    if check(i):
        bg+=1

print(bg)
