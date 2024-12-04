def xmas_count(matrix):
    final = 0
    dir = [[-1,1],[-1,-1]]
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            res = 0
            for d in dir:
                r1 = i + d[0]
                r2 = i - d[0]
                c1 = j + d[1]
                c2 = j - d[1]
                if r1>=0 and r1<m and c1>=0 and c1<n and r2>=0 and r2<m and c2>=0 and c2<n and matrix[i][j]=="A":
                    if (matrix[r1][c1]=="M" and matrix[r2][c2]=="S") or (matrix[r1][c1]=="S" and matrix[r2][c2]=="M"):
                        res += 1
            if res == 2:
                final += 1
    return final
                    
                    



def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

file_path = "/Users/smituplenchwar/Documents/AUC2024/4/advcode4.txt"  
matrix = read_matrix_from_file(file_path)

print(xmas_count(matrix))



#print(matrix)

#print(matrix[0])