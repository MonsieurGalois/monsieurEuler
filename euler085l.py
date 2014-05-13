# -*- coding: utf-8 -*-
'''
Un rectángulo de a*b contiene (a+1)(b+1) vértices por los que se intersectan los
cuadrados de lado 1x1. Si tomamos un punto de ahí, el otro debe ser un punto que 
no esté en su fila o columna, entonces debemos tomar un número entre los 

                            a*b+a+b+1-a-b+1

restantes.Claro, los rectángulos se repiten 4 veces, una por cada vértice de éste.
La idea es obtener los números a,b tales que (a*b+2)*(a*b+a+b+1) y luego dividirlo
entre 4.
'''

for a in range(10,100000):
    g=0
    for b in range(a,100000):
        f=(a+1)*(b+1)*(a*b)/4.
        t=f-2000000
        if abs(t)<10:
            print a,b,f
            print t,a*b
            g=1
            break
    if g!=0:
        break