R=[]
with open(r'C:\Users\Monsieur Galois\Github\PythonPrograms\poker.txt','rt') as poker:
    for line in poker:
        R.append([i for i in line[0:-1].split(' ')])
################################################################################
N=[str(i) for i in range(2,10)]
L=['T','J','Q','K','A']
N=N+L
N=[0,1]+N
################################################################################
def bettercard(P):
    HH=[P[j][0] for j in range(len(P))]
    t=True
    for i in range(len(N)-1,0,-1):
        if HH.count(N[i])>0:
            t=N[i]
            break
    if t!= True:
        return t
################################################################################
def twin(P):
    HH=[P[j][0] for j in range(len(P))]
    HHH=list(set(HH))
    if len(HHH)==4:
        t=0
        for i in range(len(HHH)):
            if HH.count(HHH[i])==2:
                t=HHH[i]
            if t!=0:
                break
        if t!=0:
            return t
        else:
            return 0
    else:
        return 0
################################################################################
def dtwin(P):
    HH=[P[j][0] for j in range(len(P))]
    HHH=list(set(HH))
    t1=0
    t2=0
    for i in HHH:
        if HH.count(i)==2:
            if t1==0:
                t1=i
            else:
                t2=i
        if t2!=0:
            break                
    if t2!=0:
        if N.index(t1)>N.index(t2):
            return t1
        else:
            return t2
    else:
        return 0
################################################################################
def threesame(P):
    HH=[P[j][0] for j in range(len(P))]
    HHH=list(set(HH))
    if len(HHH)==3:
        g=0
        for i in HHH:
            if HH.count(i)==3:
                g+=1
                return i
        if g==0:
            return 0
    else:
        return 0
################################################################################
def straigh(P):
    HH=[P[j][0] for j in range(len(P))]
    HHH=list(set(HH))
    HHH.sort()
    if len(HHH)==5:
        if HHH.count('T')>0:
            r=HHH.index('T')
            g=HHH.pop(r)
            HHH=HHH+[g]
        if HHH.count('J')>0:
            r=HHH.index('J')
            g=HHH.pop(r)
            HHH=HHH+[g]
        if HHH.count('Q')>0:
            r=HHH.index('Q')
            g=HHH.pop(r)
            HHH=HHH+[g]                       
        if HHH.count('K')>0:
            r=HHH.index('K')
            g=HHH.pop(r)
            HHH=HHH+[g]
        if HHH.count('A')>0:
            g=HHH.pop(HHH.index('A'))
            HHH=HHH+[g] 
        t=0
        for i in range(11):
            if N[i:i+5] == HHH:
                    t=HHH[4]
                    break
            if N[i:i+5] == HHH:
                t=HHH[4]
                break
        if t!=0:
            return 1
        else:
            return 0
    else: return 0
################################################################################
def flush(P):
    HH=[P[j][1] for j in range(len(P))]
    H=list(set(HH))
    if len(H)==1:
        return 1
    else:
        return 0
################################################################################
def full(P):
    HH=[P[j][0] for j in range(len(P))]
    H=list(set(HH))
    tw=0
    thr=0
    for i in H:
        if HH.count(i)==2:
            tw=i
        if HH.count(i)==3:
            thr=i
        if (tw!=0 and thr!=0):
            break
    if (tw!=0 and thr!=0):
        return thr
    else:
        return 0
################################################################################
def four(P):
    HH=[P[j][0] for j in range(len(P))]
    HHH=list(set(HH))
    t=0
    for w in HHH:
        if HH.count(w)==4:
            t+=1
            return w
    if t==0:
        return 0
################################################################################CORRECTO
def strflush(P):
    JJ=[P[j][1] for j in range(len(P))]
    JJJ=list(set(JJ))
    if len(JJJ)==1:
        F=straigh(P)
        if F!=0:
            return straigh(P)
        else:
            return 0
    else:
        return 0
################################################################################CORRECT
def royal(P):
    HH=[P[j][0] for j in range(len(P))]
    II=[P[j][1] for j in range(len(P))]
    II=list(set(II))
    if len(II)==1:
        Y=['T','J','K','Q','A']    
        t=1
        for i in Y:
            if HH.count(i)==0:
                t=0
                break
        if t==0:
            return 0
        else:
            return 1
    else:
        return 0
################################################################################
def win(P1,P2):
    #PP1=[full(P1),flush(P1),straigh(P1),threesame(P1),dtwin(P1),twin(P1),bettercard(P1)]
    #PP2=[full(P2),flush(P2),straigh(P2),threesame(P2),dtwin(P2),twin(P2),bettercard(P2)]
    winner=0
    PP1=[royal(P1),strflush(P1),four(P1),full(P1),flush(P1),straigh(P1),threesame(P1),dtwin(P1),twin(P1),bettercard(P1)]
    PP2=[royal(P2),strflush(P2),four(P2),full(P2),flush(P2),straigh(P2),threesame(P2),dtwin(P2),twin(P2),bettercard(P2)]
    
    for i in range(len(PP1)):
        P1P,P2P=PP1[i],PP2[i]
        if N.index(P1P)> N.index(P2P):
            winner='P1'
            break
        elif N.index(P1P)<N.index(P2P):
            winner='P2'
            break

    if winner==0:
        if PP1[9]>PP2[9]:
            winner='P1'
        else:
            winner='P2'
    return winner
################################################################################
z=0
for p in range(len(R)):
    h=R[p]
    P1=h[:5]
    P2=h[5:]
    u=straigh(P1)
    v=win(P1,P2)
    if v=='P1':
        print P1,P2, win(P1,P2)
        z+=1
print z