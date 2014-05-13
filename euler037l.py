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

ZP=[2,3,5]
o=[0,4,6,8,5]

for l in xrange(3,len(K)):
    P=K[l]
    M=str(P)
    if M[0]=='1' or M[-1]=='1':
        pass
    if M[0]=='9' or M[-1]=='9':
        pass
    else:
        for r in xrange(len(o)):
            u=o[r]
            if u !=5:
                uu=str(u)
                tt=M.count(uu)
                if tt > 0:
                    break
            else:
                uu=str(u)
                tt=M.count(uu)
                if tt>0:
                    if M[0]=='5' and len(M)<3:
                        tt-=1
                    break
        if tt==0:
            ZP.append(P)

ZPP=[]
for w in xrange(len(ZP)):
    F=str(ZP[w])
    E=len(F)
    t=1
    for j in xrange(1,E):
        W=F[j:]
        if W=='':
            break
        W=int(W)
        if K.count(W)==0:
            t=0
            break
    if t==1:
        ZPP.append(ZP[w])
QQ=[]
for v in xrange(len(ZPP)):
    M=str(ZPP[v])
    E=len(M)
    t=1
    for x in xrange(E-1,0,-1):
        MM=M[:x]
        if MM=='':
            break
        MM=int(MM)
        if K.count(MM)==0:
            t=0
            break
    if t==1:
        QQ.append(ZPP[v])
        if len(QQ)==15:
            break
        
print sum(QQ)-17
print time.time()-start