import time
start=time.time()
t=True
n=11
while t==True:
    n+=1
    N=[x for x in str(n)]
    n6=6*n
    N6=[x for x in str(n6)]
    N.sort()
    N6.sort()
    if  N==N6:
        for g in range(2,6):
            nk=g*n
            NK=[x for x in str(nk)]
            NK.sort()
            if NK != N:
                break
        if g==5 and NK==N:
            print n
            break
print time.time()-start