from queue import Queue

def read_input(path):
    matrix = []
    with open(path, "r") as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

def fence(matrix):
    dir = [[0,1],[1,0],[-1,0],[0,-1]]
    m = len(matrix)
    n = len(matrix[0])
    q = Queue()
    sum = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i,j) not in visited:
                temp = matrix[i][j]
                area = 0
                peri = 0
                q.put([i,j])
                area += 1
                visited.add((i,j))
                while (not q.empty()):
                    curr = q.get()
                    for d in dir:
                        r = curr[0] + d[0]
                        c = curr[1] + d[1]
                        if (r<0 or r>=m or c<0 or c>=n or matrix[r][c] != matrix[i][j]):
                            peri += 1
                        if r>=0 and r<m and c>=0 and c<n and matrix[r][c]== temp and ((r,c) not in visited):
                            area += 1
                            visited.add((r,c))
                            q.put([r, c])
                sum += peri * area
    return sum

path = "/Users/smituplenchwar/Documents/AOC2024/12/advcode12.txt"

matrix = read_input(path)

print(fence(matrix))



