cipher=open("cipher1.txt")
for line in cipher:
    CIP=([i for i in line[0:-1].split(',')])
cip=map(int,CIP)
cipher.close()

def decode(C,code):
    S=[]
    for a in range(0,len(C)-1,3):
        S.append(C[a]^code[0])
        S.append(C[a+1]^code[1])
        S.append(C[a+2]^code[2])
    S.append(C[-1]^code[0])
    return S
def traduce(K):
    F=map(chr,K)
    n=''
    for f in F:
        n=n+f
    return n
firstkey=[]
for i in range(97,123):
    u=0
    g=[]
    for n in range(0,len(cip),3):
        d=cip[n]
        f=d^i
        g.append(f)
        if f>126 or f<31:
            u=1
    if u==0:
        firstkey.append(i)
        
secondkey=[]
for i in range(97,123):
    u=0
    g=[]
    for n in range(1,len(cip),3):
        d=cip[n]
        f=d^i
        g.append(f)
        if f>126 or f<31:
            u=1
    if u==0:
        secondkey.append(i)
        
thirdkey=[]
for i in range(97,123):
    u=0
    g=[]
    for n in range(2,len(cip),3):
        d=cip[n]
        f=d^i
        g.append(f)
        if f>126 or f<31:
            u=1
    if u==0:
        thirdkey.append(i)

for a in firstkey:
    for b in secondkey:
        for c in thirdkey:
            T=decode(cip,[a,b,c])
            G=traduce(T)
            if 'and' in G and 'the' in G:
                print G,[a,b,c]
                print "Code:", [a,b,c]
                print "Answer=", sum(T)
