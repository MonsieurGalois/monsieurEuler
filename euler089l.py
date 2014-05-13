R=[]
with open(r'C:\Users\Monsieur Galois\Github\PythonPrograms\roman.txt','rt') as roman:
    for line in roman:
        R.append(line[0:-1])
print R
RR=[]
t=0
for i in range(len(R)):
    W=R[i]
    if 'DCCCC' in W:
        W = W.replace('DCCCC','CM')
    if 'CCCC' in W:
        W = W.replace('CCCC','CD')
    if 'LXXXX' in W:
        W = W.replace('LXXXX','XC')
    if 'XXXX' in W:
        W = W.replace('XXXX','XL')
    if 'VIIII' in W:
        W = W.replace('VIIII','IX')
    if 'IIII' in W:
        W = W.replace('IIII','IV')
    t+=len(R[i])-len(W)
print t