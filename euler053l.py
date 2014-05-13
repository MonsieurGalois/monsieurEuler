from time import time
import scipy.misc as misc
g=time()
C=0
for i in range(1,101):
    for j in range(1,101):
        if misc.comb(i,j)>1000000:
            C+=1
print C
print time()-g