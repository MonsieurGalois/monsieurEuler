A=[]
for i in range(2,100):
    for j in range(2,200):
        L=sum((int(s) for s in str(i**j)))
        if L==i:
            A.append(i**j)
            
A.sort()
print A[29]