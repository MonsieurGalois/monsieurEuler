def hexx(n):
    return n*(2*n-1)
def pen(n):
    return n*(3*n-1)/2
def tri(n):
    return n*(n+1)/2

t=285
while t:
    t+=2
    a=t
    b=(1/6.0)*((((12*t**2 +12*t+1)**.5))+1)
    c=(t+1)/2
    g=tri(a)
    if b%1==0:
        break
print tri(a),a
print hexx(c),c
print pen(b),b