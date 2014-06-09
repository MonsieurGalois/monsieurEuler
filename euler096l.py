A=open('sudoku.txt')
B=[]
for line in A:
	if line[0]=='G':
		pass
	else:
		B.append([i for i in line[0:-1].split()])

tableros=[]

while len(B)!=0:
		TT=[]
		for i in range(9):
			f=B.pop(0)
			TT.append(f)
		tableros.append(TT)

################################################################
#Lo convierto a tablero de 9x9


def ToSudoku(B):
	T=[[set([1,2,3,4,5,6,7,8,9]) for i in range(9)] for i in range(9)]
	for i in range(9):
		I=B[i][0]
		for j in range(9):
			if I[j]!='0':
				T[i][j]=int(I[j])
	return T

def verifica(n):
	t=True
	for i in range(9):
		C=set(filter(lambda x: type(x)==int,n[i]))
		if len(C)!=9:
			t=False
			break
	return t
####################################################
#Opero en los cuadritos de 3x3 


def cuadrito(n):
	for i in range(0,9,3):
		for j in range(0,9,3):
			A=set(filter(lambda x: type(x)==int,n[i][j:j+3]+n[i+1][j:j+3]+n[i+2][j:j+3]))
			for k in range(i,i+3):
				for l in range(j,j+3):
					if type(n[k][l])==set:
						n[k][l]=n[k][l].difference(A)
						if len(n[k][l])==1:
							n[k][l]=n[k][l].pop()
####################################################
#Opero en las lineas del tablero


def linea(n,j):
	A=set(filter(lambda x: type(x)==int,n[j]))
	for i in range(9):
		if type(n[j][i])==set:
			n[j][i]=n[j][i].difference(A)
			if len(n[j][i])==1:
				n[j][i]=n[j][i].pop()
####################################################
#Opero en las columnas del tablero.


def columna(n,j):
	F=[]
	for i in range(9):
		F.append(n[i][j])
	F=set(filter(lambda x: type(x)==int,F))
	for p in range(9):
		if type(n[p][j])==set:	
			n[p][j]=n[p][j].difference(F)
			if len(n[p][j])==1:
				n[p][j]=n[p][j].pop()
####################################################
#Realizo las operaciones previamente definidas para hacer los casos posibles


def solveSudo(n):
	for j in range(10):
		for i in range(9):
			linea(n,i)
			columna(n,i)
			cuadrito(n)
####################################################
#Testeo si el tablero es legal y si ya esta terminado.


def testing(n):
	L=[]
	for i in range(9):
		for j in range(9):
			if type(n[i][j])==set:
				if len(n[i][j])==2:
					L.append([i,j])
	return L
####################################################
#Realizo las operaciones mientras sea posible, pues solveSudo solo hace la iteracion una vez por parte.


def resolviendo(J):
	while verifica(J)==False:
		K=[]
		for j in J:
			K.append(j)
		solveSudo(J)
		if K==J:
			return testing(J)
			break
#####################################################


def mierda(n):
	T=[]
	for i in n:
		t=[]
		for x in i:
			if type(x)==int:
				t.append(x)
			else:
				t.append(0)
		t.reverse()
		T.append(t)
	return T

def mierda2(n):
	A=[]
	for i in n:
		for j in i:
			if type(j)==set:
				A.append(len(j))
	return A



#Parte estancada.


for z in range(20):
	#for j in range(9):
		#print tableros[i][j]
	J=ToSudoku(tableros[z])
	S=resolviendo(J)
	if verifica(J)==False:
		for i in S:
			T=ToSudoku(tableros[z])
			resolviendo(T)
			lm=list(J[i[0]][i[1]])
			T[i[0]][i[1]]=lm[0]
			resolviendo(T)
			if verifica(T)==True:
				J=T
				break
			else:
				T=ToSudoku(tableros[z])
				S=resolviendo(T)
				T[i[0]][i[1]]=lm[1]
				resolviendo(T)
				if verifica(T)==True:
					J=T
					break
		if verifica(J)==False:
			print mierda2(J)

