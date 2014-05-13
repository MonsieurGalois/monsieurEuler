import time
start=time.time()
A17=[17*x17 for x17 in range(1,1000/17)]
A13=[13*x13 for x13 in range(1,1000/13)]
A11=[11*x11 for x11 in range(1,1000/11)]
A7=[7*x7 for x7 in range(2,1000/7)]
A5=[5*x5 for x5 in range(3,1000/5)]
A3=[3*x3 for x3 in range(4,1000/3)]
A2=[2*x2 for x2 in range(5,1000/2)]
B=[A17,A13,A11,A7,A5,A3,A2]
def fil5(n):
    if ((n/10)%10)%5==0:
        return True
    else:
        return False
B[3]=filter(fil5,B[3])

def fil2(n):
    if (n/100)%2==0:
        return True
    else:
        return False
B[4]=filter(fil2,B[4])

def fil2d(n):
    if ((n/10)%10)%2==0:
        return True
    else:
        return False
B[5]=filter(fil2d,B[5])

def dstr(n):
    L=[x for x in n]
    if len(L) != len(set(L)):
        return False
    else:
        return True
B[0]=map(str,B[0])
B[1]=map(str,B[1])
B[2]=map(str,B[2])
B[3]=map(str,B[3])
B[4]=map(str,B[4])
B[5]=map(str,B[5])
B[6]=map(str,B[6])

for T in B:
    for k in range(len(T)):
        if len(T[k])<3:
            T[k]='0'+T[k]


B[0]=filter(dstr,B[0])
B[1]=filter(dstr,B[1])
B[2]=filter(dstr,B[2])
B[3]=filter(dstr,B[3])
B[4]=filter(dstr,B[4])
B[5]=filter(dstr,B[5])
B[6]=filter(dstr,B[6])
F=[x+y+z for x in B[6] for y in B[3] for z in B[0] ]
F=filter(dstr,F)


FF=[]
for s in F:
    if s[1:4] in B[5]:
        FF.append(s)
                                #En esta parte ya estan los multiplos de 17 los de 7 , los de 2 y los de 3    
FFF=[]
for s in FF:
    if s[4:7] in B[2]:
        FFF.append(s)
                                #Multiplos de  17  ,  7  ,  11  ,  2  ,  3
FFFF=[]
for s in FFF:
    if s[5:8] in B[1]:
        FFFF.append(s)
                                #Multiplos de 17  ,  7  ,  11  ,  2  ,  3  ,  13
L=[]                                
for s in FFFF:
    if s[2:5] in B[4]:
        L.append(s)


for i in range(len(L)):
    l=L[i]
    H=[q for q in str(l)]
    H=map(int,H)
    for z in range(10):
        if not(z in H):
            L[i]=z*10**9+int(l)
            break
print L
print sum(L)
print time.time()-start