import fractions as fr

t=0
ai = fr.Fraction(2)
bi = 1
n = 10
for i in range(n):
    ai = 2 + bi / ai
    print ai
    F = ai - 1
    den=F.denominator
    num=F.numerator
    if len(str(num))>len(str(den)):
        t+=1
print t