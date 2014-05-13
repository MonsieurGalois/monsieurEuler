r4=0
for i in range(10,100):
    a=[m for m in str(i)]
    for j in range(10,100):
        if r4==4:
            break
        if i==j:
            continue
        else:
            b=[u for u in str(j)]    
            x=int(a[0])
            y=int(a[1])
            w=int(b[0])
            z=int(b[1])
            p= x==w 
            q= x==z 
            r= y==w 
            s= y==z
            if z==0 or w==0:
                pass
            else:
                if (p or q or r or s)==True and (x or y or z or w) !=0:
                    
                    if p==True:
                        if float(y)/int(z)==float(i)/j:
                            print i,j
                            print 'la pareja es', y,y
                            r4+=1
                            continue
                    if q==True:
                        if float(y)/int(w)==float(i)/j:
                            print i,j
                            r4+=1
                            continue
                    if r==True:
                        if float(x)/int(z)==float(i)/j:
                            print i,j
                            r4+=1
                            continue
                    if s==True:
                        if float(x)/int(w)==float(i)/j:
                            print i,j
                            r4+=1
                            continue