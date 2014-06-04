from numpy import zeros
from time import time
t=time()
R=[]
neo=open('matrix.txt')
for line in neo:
    R.append(map(int,line[0:-1].split(',')))

M=zeros((80,80))

for a in range(len(M)):
    for b in range(len(M)):
        M[a,b]=R[a][b]
        
#a fila/ b columna

N=zeros((80,80))
N[0,:]=M[0,:]

for i in range(80):
    for j in range(80):
        
        P=[]
        for r in range(80):
            if r==j:
                P.append(N[i-1,j]+M[i,j])

            elif r<j:
                P.append( N[i-1,r] + sum(M[i,r:j]) + M[i,r])

            else:
                P.append( N[i-1,r] + sum(M[i,j:r]) + M[i,j])

        N[i,j]=min(P)
        
print min(N[79,:])
print N
print time()-t
