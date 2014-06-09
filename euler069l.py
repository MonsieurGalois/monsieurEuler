from euler010l import primes
from euler003l import factor

A=primes(1000000)

t=1
for i in A:
	tt=t*i
	if tt<1000000:
		t=tt
	else:
		break
	
F=factor(t)

phi=1

for j in set(F):
	phi*=(1-1/float(j))

print t
print 1/phi
print F
