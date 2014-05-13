import numpy as np
R=[]
with open(r'C:\Users\Monsieur Galois\Github\PythonPrograms\base_exp.txt','rt') as base:
    for line in base:
        R.append([i for i in line[0:-1].split(',')])

#print R
t=0
line=0
for i in range(len(R)):
    base=int(R[i][0])
    exp=int(R[i][1])
    number=exp*(np.log2(base))
    if number>t:
        t=number
        line=i
print line