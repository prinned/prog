def chk(x):                                             #| 
    for i in range(1,10):                               #v splice from first digit to penultimate digit
        try:
            if str(x)[len(str(x))-1] == str(i*x)[0] and str(x)[-1::len(str(x))-2]==str(i*x)[::len(str(x))-1]:
                    #last digit^        #^first digit of new number             #^splice from start to last digit
                return i,x*i
        except:
            
    return False


    
for i in range(10,1000):
    try:
        print(i,chk(i))
    except:
        print(i,len(str(i)))
