Q=[True]*(10**7+1)
Q[89],Q[145],Q[42],Q[20],Q[4],Q[16],Q[37],Q[58]=89,89,89,89,89,89,89,89
Q[1],Q[10]=1,1

def cuad(n):
    if n==89 or n==1 or n==1:
        return n
    else:
        L=map(int,str(n))
        LL=map(lambda x: x**2, L)
        return sum(LL)
    
def cuadchain(m):
    P=[]
    t=m
    P.append(t)
    while t != 89 and t != 1:
        t=cuad(t)
        P.append(t)
        if t<len(Q):
            if Q[t] != True:
                for i in range(len(P)):
                    r=P[i]
                    Q[r]=Q[t]
                break
        if t==89:
            for i in range(len(P)):
                r=P[i]
                Q[r]= 89
                
        if t==1:
            for i in range(len(P)):
                r=P[i]
                Q[r]=1
                
for y in xrange(2,len(Q)):
    if Q[y] == True:
        cuadchain(y)
    print y
print Q.count(89)
# 254.67 segundos del final hacia adelante sin xrange
# 253.77 segundos del final hacia adelante con xrange
# 252.24 segundos de adelante hacia el final, con xrange