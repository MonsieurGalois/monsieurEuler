import time
start=time.time()
a=1
b=1
n=2
k=False
e=range(1,10)
while k==False:
    c=a+b
    b=a
    a=c
    n+=1
    M=[x for x in str(c%10**9)]
    M=map(int, M)
    M.sort()
    if M==e:
        N=[y for y in str(c)]
        N=map(int,N[:9])
        N.sort()
        if N==e:
            k=True
print n
print time.time() -start