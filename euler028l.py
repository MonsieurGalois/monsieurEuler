n=1001

diag1=n*(n+1)*(2*n+1)/6 -500

a=1
b=0
for i in range(1001):
    a=a+2*i
    #print a
    b+=a
print diag1+b-1