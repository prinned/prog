dif = []
for i in range(1,21):
    j = i-1
    dif.append(i**3 - j**3)
    #print(i, i**3,  i**3 - j**3)

j = 0
mdif = []
for i in dif:
    mdif.append(i-j)
    print(i,i-j)
    j = i


    

