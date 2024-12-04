def xmas_count(matrix):
    final = 0
    dir = [[[-1,0],[-2,0],[-3,0]],[[1,0],[2,0],[3,0]],[[0,-1],[0,-2],[0,-3]],[[0,1],[0,2],[0,3]],[[-1,-1],[-2,-2],[-3,-3]],[[1,1],[2,2],[3,3]],[[-1,1],[-2,2],[-3,3]],[[1,-1],[2,-2],[3,-3]]]
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            for t in dir:
                count = 0
                res = 0
                for d in t:
                    r = i + d[0]
                    c = j + d[1]
                    count += 1
                    if r>=0 and r<m and c>=0 and c<n and matrix[i][j]=="X":
                        if count==1 and matrix[r][c]=="M":
                            res += 1
                        if count==2 and matrix[r][c]=="A":
                            res += 1
                        if count==3 and matrix[r][c]=="S":
                            res += 1
                if res == 3:
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