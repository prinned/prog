import csv

writer=csv.writer(open('golom.csv','w',newline=''))

#set:
ul=500000

g=[None,1]  #starting of the g set
n=1
k=0     #acts as the count, i.e., how many times left
for i in range(2,ul+1):
    if k==0:
        n+=1
        g.append(n)
        k=g[n]-1
    else:
        g.append(n)
        k-=1
while 1==1:
    x=int(input(': '))
    print(g[x],g[x**3])
