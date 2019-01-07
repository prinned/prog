rows = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if i+j+k+l==12:
                    rows.append([i,j,k,l])
print("rows done")

squares=[]
for i in rows:
    print(i)
    for j in rows:
        for k in rows:
            for l in rows:
                print(l)
                for x in range(4):
                    if i[x]+j[x]+k[x]+l[x] ==12 and i[0]+j[1]+k[2]+l[3]==12 and i[3]+j[2]+k[1]+l[0]==12:
                        squares.append([i,j,k,l])
