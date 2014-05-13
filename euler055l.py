from time import time
Lchrel=9999
ss=time()
Lch=[]
for i in range(1,10000):
    t=0
    ii=str(i)
    while t<51:
        t+=1
        iii=int(ii[::-1])
        ii=int(ii)
        I=ii+iii
        II=str(I)
        if II==II[::-1]:
            break
        else:
            ii=II
    if t<50:
        Lchrel-=1
    else:
        Lch.append(i)
print Lchrel
print time()-ss