U=['','one','two','three','four','five','six','seven','eight','nine']
D=['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
D10=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
H='hundred'
AND='and'
t=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            n=j*100+k*10+i
            if j==0:
                if k==1:
                    L=D10[i]
                    t+=len(L)
                    print n,L
                else:
                    L=D[k]+U[i]
                    t+=len(L)
                    print n,L
            else:
                if k==0 and i==0:
                    L=U[j]+H
                    t+=len(L)
                    print n,L
                else:
                    if k==1:
                        L=U[j]+H+AND+D10[i]
                        t+=len(L)
                        print n,L
                    else:
                        L=U[j]+H+AND+D[k]+U[i]
                        t+=len(L)
                        print n,L
print t+11