import random
n=int(input('Enter the number of columns in the matrix 1:'))
m=int(input('Enter the number of rows in the matrix 1:'))
k=int(input('Enter the number of columns in matrix 2:'))

m1=[[random.randint(0,5)for i in range(n)]for j in range(m)]
m2=[[random.randint(0,5)for i in range(k)]for j in range(n)]
res=[[0 for i in range(k)]for j in range(m)]

print('Matrix 1:')
for i in range(m):
    for j in range(n):
        print(m1[i][j],end=' ')
    print()

print('Matrix 2:')
for i in range(n):
    for j in range(k):
        print(m2[i][j],end=' ')
    print()

for i in range(m):
    for j in range(k):
        for z in range(n):
            res[i][j]+=(m1[i][z]*m2[z][j])
print('Multiply the matrix: ',res)
