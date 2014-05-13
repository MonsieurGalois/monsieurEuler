'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

                            a**2 + b**2 = c***2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
for i in range(1,1000):
    for k in range(3,999):
        r=1000-i-k
        if i**2+k**2==r**2:
            print i,k,r
            print i*k*r
