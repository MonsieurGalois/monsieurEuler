# -*- coding: utf-8 -*-
'''
El perimetro es 3*i+1.

El área es con la fórmula de Herón, que es :

        (p*(p-i)*(p-i)*(p-i-1))**.5
        
        3*i+1        3*i+1
        -----        ----- 
          2            2
Que podemos verla como:
    
        (i+1)   *   (   (3*i+1)   *   (i-1)   )**.5
        ---------------------------------------
                            4

Para ahorrar cuentas, en vez de calcular la multiplicación, le sumaré 3 a la operación,
y el área será con heron'''

side=3
perimeter=10
sumperimeters=0
area=0
while side<333333333:
    side+=1
    perimeter+=3
    area=((side+1)*(perimeter*(side-1))**.5)/4.
    if area%1==0:
        print side
        sumperimeters+=perimeter
print side, 'lado final'
print area,'final'
print sumperimeters,'perimetros'