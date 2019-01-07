import csv

prl=[]
with open('E:/prog/primer.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        for i in row:
            prl.append(int(i))
            
def rem(n):
    pnm=pow(prl[n-1]-1,n,prl[n-1]**2)
    ppm=pow(prl[n-1]+1,n,prl[n-1]**2)
    return (ppm+pnm)%prl[n-1]**2

for i in range(40000):
    if rem(i) > 10000000000:
        print('I found it, check: ', i)
        break

