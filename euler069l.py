from euler010l import primes
from euler003l import factor

A=set(primes(1000000))

def orderfactor(n):
	F=factor(n)
	Q=dict()
	for i in set(F):
		Q[i]=F.count(i)
	return Q	

PHIS=[True]*100
PHIS[0]=0
PHIS[1]=1
for i in A:
	p=i
	while p<1000001:
		PHIS[p]=		

print PHIS
