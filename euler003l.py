import time
def factor(t):
    if t==0:
	return 'There is no factorization for 0'
    else:
	a=[]
        while t%2==0:
            t=t/2
            a=a+[2]
        for i in range(3,int(t**.5)+1,2):
            if t<=1:
                break
            else:
                while t%i==0:
                    a=a+[i]
                    t=t/i
        if t==1:
	    return a
	else:
	    a=a+[t]
            return a

k = time.time()
#print factor(65765323)
print factor(600851475143 )
#for i in range(2000,2050):
#    print i, factor(i)
#print factor(2014)

b= time. time()
