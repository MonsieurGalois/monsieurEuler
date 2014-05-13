R=[]
with open(r'C:\Users\Monsieur Galois\Github\PythonPrograms\triangles.txt','rt') as triangles:
    for line in triangles:
        R.append([i for i in line[0:-1].split(',')])
for i in range(len(R)):
    R[i]=map(int,R[i])
    
def trianglearea(a,b,c):
    return .5*abs((a[0]-c[0])*(b[1]-a[1])-(a[0]-b[0])*(c[1]-a[1]))
def trianglezero(a,b):
    return .5*abs(b[0]*a[1]-b[1]*a[0])
total=0
for j in R:
    x=j[0:2]
    y=j[2:4]
    z=j[4:6]
    ABC=trianglearea(x,y,z)
    OABC=trianglezero(x,y)+trianglezero(x,z)+trianglezero(y,z)
    print ABC,OABC
    if ABC==OABC: total+=1
print total