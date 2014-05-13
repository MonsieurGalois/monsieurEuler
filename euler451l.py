from fractions import gcd
import time as ti
start=ti.time()
def primes(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for f in xrange(len(S)):
        if S[f]==True:
            P.append(f)
            for m in xrange(2,n/f+1):
                if m*f<len(S):
                    S[m*f]=False
    return P
K=primes(2*10**7)

def con1(n):
    for p in range(n-2,0,-1):
        if gcd(p,n)==1:
            t=(p**2-1)%n
            if t==0:
                break
    return p
e=0
for j in xrange(3,2*10**7+1):
    if j in K:
        e+=1
    else:
        e+=con1(j)
    print j,con1(j)

print e
print ti.time()-start