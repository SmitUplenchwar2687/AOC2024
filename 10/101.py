def read_input(path):
    matrix = []
    with open(path, 'r') as file:
        for line in file:
            row = [int(i) for i in line.strip()]
            matrix.append(row)
    return matrix

def trailheads(matrix):
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                visited = set()
                count += helper(matrix, [i,j], visited)
    return count

def helper(matrix, curr, visited):
    i = curr[0]
    j = curr[1]
    m = len(matrix)
    n = len(matrix[0])
    if matrix[i][j] == 9 and (i,j) not in visited:
        visited.add((i, j))
        return 1
    
    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    total_count = 0
    for d in dir:
        r = i + d[0]
        c = j + d[1]
        if r>=0 and r<m and c>=0 and c<n and matrix[r][c]-1 == matrix[i][j]:
            total_count += helper(matrix, [r,c], visited)
    return total_count
    

path = "/Users/smituplenchwar/Documents/AOC2024/10/advcode10.txt"
matrix = read_input(path)

print(trailheads(matrix))