ul = 100

sqsm = 0
smsq = 0
for i in range(1,ul+1):
    sqsm+= i**2
    smsq += i
print(smsq**2-sqsm)
