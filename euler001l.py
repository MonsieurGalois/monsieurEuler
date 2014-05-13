A=[k for k in range(3,1000,3)]
B=[k for k in range(5,1000,5)]
C=set(A+B)
C=list(C)
print sum(C)
