import time
k=time.time()
a=[10**i for i in range(2,18)]
print a[0]
for i in xrange(10**8+10**6+1,14*10**7,2):
    if i%10==3 or i%10==7:
        n=i**2
        if n%a[1]/a[0] - 8 ==0:
            if n%a[3]/a[2] - 7 ==0:
                if n%a[5]/a[4] - 6 ==0:
                    if n%a[7]/a[6] - 5 ==0:
                        if n%a[9]/a[8] - 4 ==0:
                            if n%a[11]/a[10] - 3 ==0:
                                if n%a[13]/a[12] - 2 ==0:
                                    if n%a[15]/a[14] - 1 ==0:
                                        print i*10
                                        break
print time.time()-k