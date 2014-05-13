'''

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''

import time
a=time.time()
m=2**1000
C=[int(i) for i in str(m)]
sum(C)
b=time.time()
print sum(C)
print b-a
