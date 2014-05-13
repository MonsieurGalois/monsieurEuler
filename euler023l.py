import time
sss=time.time()
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
K=primes(28123)

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
    
A=[]
for i in range(12,28123):
    if not (i in K):
        if sumdiv(i)>i:
            A.append(i)
a=max(A)
F=[]
for j in range(len(A)):
    g=A[j]
    for jj in range(j,len(A)):
        b=A[jj]
        if g+b<a or g+b==a:
            F.append(g+b)
F=list(set(F))
e=0
for y in range(1,28123):
    if not y in F:
        e+=y
print e
print time.time()-sss