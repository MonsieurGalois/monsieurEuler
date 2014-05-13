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
K=primes(10000)
def sumdiv(t):
    s=t
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
    if t!=1:
        a=a+[t]
    g=list(set(a))
    h=[]
    for n in range(len(g)):
        r=a.count(g[n])
        h.append(r+1)
    e=1
    for c in range(len(h)):
        e*=(g[c]**(h[c])-1)/(g[c]-1)
    return e-s

amig=[]
L=[True]*10001
L[0]=0
L[1]=0
L[6],L[28]=6,28
for i in range(len(K)):
    p=K[i]
    L[p]=1
for j in range(len(L)):
    if L[j]==True:
        q=sumdiv(j)
        L[j]=q
        if q<10000:
            if L[q]==j  and q!=j:
                amig.append(q)
                amig.append(j)
print sum(amig)
print amig

for i in range(len(amig)):
    print amig[i],sumdiv(amig[i])
