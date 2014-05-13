from time import time
start=time()
def divs(t):
    s=t
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
    return len(g)


T=0
f=0
e1=divs(f+1)
e2=divs(f+2)
e3=divs(f+3)
e4=divs(f+4)
while T==0:
    f+=1
    e1=e2
    e2=e3
    e3=e4
    e4=divs(f+4)
    if e1==4 and e2==4 and e3==4 and e4==4:
        print f,e1,e2,e3,e4
        T=1
print time()-start