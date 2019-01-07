f=[1,2]
for i in range(2,10000):
    f.append(f[i-1]+f[i-2])
    i+=1

bg=0
for i in f:
    if i%2==0 and i<4000000:
        bg+=i

print(bg)
    
    
