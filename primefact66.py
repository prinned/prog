import csv

with open('prime.csv','r') as file:
    reader=csv.reader(file)
    prim=[]
    for row in reader:
        for i in row:
           prim.append(i)
    prim=prim[::-1]
    
def hpf(n):
    
