from decimal import getcontext,Decimal
getcontext().prec=10002

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
K=primes(10**3)
nmax=0
trivial=4
maxd=trivial
for i in xrange(999,12,-1):
    print i
    trivial=4
    F=Decimal(1.)/Decimal(i)
    if i in K:
        L=[x for x in str(F)]
        T=False
        while T==False:
            #print L[2:maxd]
            #print L[maxd:2*maxd-2]
            if L[2:trivial]!=L[trivial:2*trivial-2]:
                trivial+=1
                if trivial>maxd: 
                    maxd=trivial
                    nmax=i
            else: T=True
print maxd,nmax