from time import time
aa=time()
C=[i**3 for i in range(22,100000)]
strs=[]
for i in xrange(len(C)):
    f=[str(d) for d in str(C[i])]
    f.sort()
    strs.append(f)

for m in xrange(len(strs)):
    gg=strs.count(strs[m])
    if gg==5:
        break
print C[m],strs[m],m
print time()-aa