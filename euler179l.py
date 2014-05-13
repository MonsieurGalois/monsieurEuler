F=[True]*10**7

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
    return S
K=primes(10**7)
K[0]=0
K[1]=1
for i in range(len(K)):
    if K[i]!=0:
        for p in K[K[i]:]:
            if p*i<10**7:
                K[i*p]=4
                
print K