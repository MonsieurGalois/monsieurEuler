import time
start=time.time()
def primes(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for i in xrange(len(S)):
        if S[i]==True:
            P.append(i)
            for m in xrange(2,n/i+1):
                if m*i<len(S):
                    S[m*i]=False
    return P
K=primes(10**4)
n=0
i=0
while n<len(K):
    e=1000-K[i]
    if e>0:
        K.remove(K[i])
        i-=1
    else:
        break
    i+=1
    
T=False
for i in xrange(len(K)):
    f=K[i]
    if f==1487 or f==4817 or f==8147:
        pass
    else:
        U=[x for x in str(f)]
        U.sort()
        for m in xrange(900,8000,6):
            f2=f+m
            U2=[x for x in str(f2)]
            U2.sort()
            if K.count(f2)>0 and U2==U:
                f3=f2+m
                U3=[x for x in str(f3)]
                U3.sort()
                if K.count(f3)>0 and U3==U2:
                    print f*100000000+f2*10000+f3
                    T=True
                    break
    if T==True:
        break
print time.time()-start