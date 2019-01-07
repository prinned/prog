'''This program finds the largest palindrome which is a
product of two 3-digit numbers. E2018/'''

import math

def palchk(i):  #checks whether i is a palindrome
    ja = ""

    for m in range(0,len(str(i))//2):
        ja += str(i)[m]  #ja = first half of number

    jb = ""
    for m in range(math.ceil(len(str(i))/2),len(str(i))):
        jb += str(i)[m] #jb = second half of number

    if(ja==jb[::-1]):
        return True

bg=0
for i in range(100,1000):
    for j in range(100,1000):
        if palchk(i*j) and i*j > bg:
            bg = i*j

print(bg)
