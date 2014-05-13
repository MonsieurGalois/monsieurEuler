y=1900
su=0
d=365%7
cmd=[3,0,3,2,3,2,3,3,2,3,2,3]
cmd4=[3,1,3,2,3,2,3,3,2,3,2,3]
while y<2000:
    if y%4==0 and (not (y%400==0)):
        for i in range(len(cmd4)):
            d+=cmd4[i]
            if d%7==0:
                su+=1
    else:
        for i in range(len(cmd)):
            d+=cmd[i]
            if d%7==0:
                su+=1
    y+=1
    d%=7
    print d
print su
'''
Enero           31              3
Febrero     28                  0
Marzo           31              3
Abril               30          2       
Mayo            31              3
Junio               30          2
Julio           31              3
Agosto          31              3
Septiembre          30          2
Octubre         31              3
Noviembre           30          2
Diciembre       31              3

'''