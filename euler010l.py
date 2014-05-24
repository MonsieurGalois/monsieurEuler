import time

def primes(n):
	i=2
	P=[]
	S=[True]*n
	S[0],S[1]= False, False
	while i<n:
		if S[i]==True:
			P.append(i)
			t=2
			while t*i<n:
				S[t*i]=False
				t+=1 
		i+=1
	return P

	

'''
r=1000000000
comienzo=time.time()
primes(r)
final=time.time()
print "Tiempo tardado :D :" , final - comienzo
'''
