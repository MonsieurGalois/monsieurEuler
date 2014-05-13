from time import time
g=time()
maxnum=0
maxmax=0
for i in range(1,9877):
    T=''
    for p in range(1,10):
        T+=str(i*p)
        if '0' in T:
            break
        if int(T)>maxnum:
            F=[x for x in str(T)]
            F.sort()
            F=map(int,F)
            if F==range(1,10):
                maxnum=int(T)
                maxmax=i
                break
print maxnum,maxmax
print time()-g