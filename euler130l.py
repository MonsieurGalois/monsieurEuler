def primes(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for i in xrange(len(S)):
        if S[i]==True:
            P.append(i)
            for m in xrange(2,n/i):
                S[m*i]=False
    return P
K=primes(250000)

i=1
t=0
total=0
while t<25:
    i+=2
    if not i in K:
        if i%5!=0:
            repunit=1
            for j in range(1,i-1):
                jj=0
                repunit+=10**j
                if repunit%i==0:
                    jj+=1
                    lenunit=len(str(repunit))
                    if (i-1)%lenunit==0:
                        t+=1
                        total+=i
                        print i,repunit
                        break
                if jj!=0:
                    break
print total