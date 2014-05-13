import time
def primes(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for i in xrange(len(S)):
        if S[i]==True:
            P.append(i)
            for m in xrange(2,n/i):
                S[m*i]=False
    print sum(P)
    print P


r=1000000000
comienzo=time.time()
primes(r)
final=time.time()
print "Tiempo tardado :D :" , final - comienzo
