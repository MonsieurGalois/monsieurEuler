from time import time as ti
start=ti()
from numpy import matrix
A=matrix([[1,-2,2],[2,-1,2],[2,-2,3]])
B=matrix([[1,2,2],[2,1,2],[2,2,3]])
C=matrix([[-1,2,2],[-2,1,2],[-2,2,3]])
INIT=matrix([[3],[4],[5]])
FULL=[INIT]
F=[]
for n in FULL:
    AA=A*n
    BB=B*n
    CC=C*n
    if sum(AA)<1001:
        FULL.append(AA)
    if sum(BB)<1001:
        FULL.append(BB)
    if sum(CC)<1001:
        FULL.append(CC)

for i in range(len(FULL)):
    g=FULL[i]
    g.transpose()
    g=g.flatten().tolist()[0]
    F.append(g)    
        
for f in F:
    for z in range(1,83):
        def mult(lis):
            return [z*f[0],z*f[1],z*f[2]]
        ff=mult(f)
        if sum(ff)<1000:
            if not ff in F:
                F.append(ff)
        else:
            break
def sumi(n):
    return n[0]+n[1]+n[2]
F=map(sumi,F)

maxmax=0
MAX=0
for j in F:
    t=F.count(j)
    if t>maxmax:
        maxmax=t
        MAX=j
print maxmax
print MAX
print ti()-start