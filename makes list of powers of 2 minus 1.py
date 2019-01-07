#this prog makes a csv full of powers of 2 minus 1 and prints their factorisation
import csv

def prime_factors(n):
    i = 2
    factors = ""
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors +=str(i)
            factors += " x "
    if n > 1:
        factors += str(n)
        factors += " x "
    if prime == False:
        return factors[:-3]
    else:
        return "Prime"

with open("prime.csv",'w',newline='')as csvfile:
    writer = csv.writer(csvfile,delimiter=",")

    writer.writerow(["a","2^a - 1", "Prime?","Factorization"])
    for a in range(1,25):
        mer = 2**a -1

        #prime-check
        prime = True
        for i in range(2,mer):
            if mer % i == 0:
                prime = False

        #prime-check/
                

        writer.writerow([a,mer,prime,prime_factors(mer)])

