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
K=primes(10**6)
ZP=[2,5]
o=[0,2,4,5,6,8]
for l in range(len(K)-1):
    P=K[l]
    M=str(P)
    for r in range(6):
        u=o[r]
        uu=str(u)
        tt=M.count(uu)
        if tt != 0:
            break
    if tt==0:
        ZP.append(P)
ZPP=[]
for w in range(len(ZP)):
    t=1
    W=str(ZP[w])
    E=len(str(ZP[w]))
    for j in range(E):
        W=str(W)
        Q=W        
        W=W[1:]
        W=W+Q[0]
        W=int(W)
        if K.count(W)==0:
            t=0
            break
            
    if t==1:
        ZPP.append(W)
print len(ZPP)
print time.time()-start
