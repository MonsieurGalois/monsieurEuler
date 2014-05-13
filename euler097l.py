from time import time
qqq=time()
def exponbin(base,exp,mod):
    N=mod
    E='{0:b}'.format(exp)
    B=1
    e=1
    for i in range(len(E)-1,-1,-1):
        if E[i]=='1':
            B*=(base**e)
            B%=N
        e*=base
        e%=N
    return B
    
U=exponbin(2,7830457,10**10)   
print (U*28433+1)%10**10, time()-qqq