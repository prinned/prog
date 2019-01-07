import math

def pck(n):
    ck=True
    if n==0 or n==1:
        ck=False
    else:
        for i in range(2,1+math.floor(math.sqrt(n))):
            if n % i == 0:    #^testing from 2 to sqrt n
                ck=False
                break
    return(ck)

def pckr(ll,ul): 
    prim=[]
    for i in range(ll,ul):
        if pck(i):
            prim.append(i)
    return prim

if __name__ == "__main__":
    while 1==1:
        
        yn = input("pckr - r, else pck: ")
        if yn == 'r':
            x = int(input("Enter ll: "))
            y = int(input("Enter ul: "))
            print(pckr(x,y))
        else:
            x = int(input("Enter: "))
            print("Is Prime: ", pck(x))           
