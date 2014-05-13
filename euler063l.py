t=0
for i in range(1,100):
    for j in range(50):
        k=i**j
        n=str(k)
        if j==len(n):        
            print n,j
            t+=1
        elif j>len(n):
            break
print t