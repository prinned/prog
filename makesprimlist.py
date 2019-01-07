import csv
import prime

with open('primer.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    prl=[]
    for i in prime.pckr(0,1000000):
        prl.append(i)
    writer.writerow(prl)
