def primes(n):
    P=[]
    S=[True]*n
    S[0],S[1]= False, False
    for i in xrange(len(S)):
        if S[i]==True:
            P.append(i)
            for m in xrange(2,n/i+1):
                if m*i<len(S):
                    S[m*i]=False
    return P
K=primes(10**6)
print 'ok'
for i in xrange(1,10**8,2):
    t=1
    if not i in K:
        for m in xrange(len(K)):
            j=K[m]
            if i-j<0:
                break
            elif (((i-j)/2.)**.5)%1==0:
                break
            else:
                if (((i-j)/2.)**.5)%1!=0 and i-K[m+1]<0 :
                    print (((i-j)/2.)**.5),K[m]
                    print i
                    t=0
                    break
            if t==0:
                break
    if t==0: break