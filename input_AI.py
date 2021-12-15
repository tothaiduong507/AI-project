R = int(input("Row size = ")) #rowsize
C = int(input("Column size = ")) #columnsize

#thiet lap so do 
matrix = []
for i in range(R):
    rowth = []
    for j in range(C):
        rowth.append([j])
    matrix.append(rowth)

#dien cac vi tri tren ban do 
print("Pls insert the map (ware house, live tree, dead tree, new seed, obstacle)")   
for i in range(R):
        rowth = input().split("  ") #nhap vao mot hang gom C doi tuong ngan cach boi "2-spaces"
        for j in range(C):
            matrix[i][j] = rowth[j]
print(matrix)
