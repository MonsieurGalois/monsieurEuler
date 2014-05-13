import time
from math import factorial as fac

a=time.time()
P=[]
for i in xrange(100,9000000):
    L=[x for x in str(i)]
    L=map(int,L)
    F=map(fac,L)
    if sum(F)==i:
        print i
        P.append(i)
print sum(P)
print time.time() -a