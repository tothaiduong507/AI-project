import random

n = random.randint(4, 9)
m = random.randint(4, 9)
matrix=[]
for i in range(n):
    c=[]
    for j in range(m):
        if i == 0 and j == 0:
            c.append(1)
            continue
        a = random.randint(0, 4)
        while a == 1:
            a = random.randint(0, 4)
        c.append(a)
    print()
    matrix.append(c)
print(str(n) + ' ' + str(m))
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = ' ')
    print()

f = open('testcase_80.txt', 'w')
f.write(str(n) + ' ' + str(m) + '\n')
for i in range(n):
    for j in range(m):
        f.write(str(matrix[i][j]) + ' ')
    f.write('\n')
f.close()
