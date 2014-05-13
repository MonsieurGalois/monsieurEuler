def factor(t):
    a=[]
    while t%2==0:
        t=t/2
        a=a+[2]
    for i in range(3,int(t**.5)+1,2):
        if t<=1:
            break
        else:
            while t%i==0:
                a=a+[i]
                t=t/i
    if t!=1:
        a=a+[t]
    g=list(set(a))
    h=[]
    for n in range(len(g)):
        r=a.count(g[n])
        h.append(r+1)
    e=1
    for c in range(len(h)):
        e*=h[c]
    return e        

D=1
i=2
y=0
while D<500:
    y+=1
    j=i
    i+=1
    Dj=D
    if i%2==0:
        Di=factor(i/2)
    else:
        Di=factor(i)
    D*=Di
    if D<500:
        D/=Dj
    if i*j/2==76576500:
        break

print i*j/2,D
