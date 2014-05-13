import decimal as dec

t=0
dec.getcontext().prec=102
for i in range(2,100):
    n=dec.Decimal(i).sqrt()
    p=pow(10,99)
    N=n*p
    N=int(N)
    M=[x for x in str(N)]
    M=map(int,M)
    t+=sum(M)
print t-44
print dec.Decimal(2).sqrt()