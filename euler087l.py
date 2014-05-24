from euler010l import primes

A=primes(300000)

SQ=filter(lambda x: x<50000000, map(lambda x: pow(x,2),A))
CU=filter(lambda x: x<50000000, map(lambda x: pow(x,3),A))
FO=filter(lambda x: x<50000000, map(lambda x: pow(x,4),A))

N=[]
for i in SQ:
	for j in CU:
		N.append(i+j)
N=set(filter(lambda x: x<50000000,N))

A=[]
for n in N:
	for m in FO:
		if n+m<50000000:
			A.append(m+n)
		else:
			break	
print len(set(A))
