import time
n=time.time()
max=0
for i in range(2,101):
    for j in range(2,101):
        a=i**j
        M=[x for x in str(a)]
        M=map(int,M)
        if max<sum(M):
            max=sum(M)
print max
print time.time()-n