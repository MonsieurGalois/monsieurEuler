LL=[]
for i in xrange(1,1000000):
    N=[s for s in str(i)]
    NN=N[::-1]
    if NN==N:
        LL.append(i)
    
Q=len(LL)-1
P=[]
for w in xrange(Q):
    J=LL[w]
    E='{0:b}'.format(J)
    EE=E[::-1]
    if E==EE:
        print J, E
        P.append(J)
print P
print sum(P)