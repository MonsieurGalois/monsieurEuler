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
f=7
K=primes(10**f)
L=len(K) 
A=[map(str,range(1,m)) for m in range(2,f+2)]

for i in xrange(L-1,-1,-1):
    PP=[x for x in str(K[i])]
    PP.sort()
    U=len(PP)
    LP=A[U-1]
    if PP==LP:
        print K[i]
        break
print time.time() -start