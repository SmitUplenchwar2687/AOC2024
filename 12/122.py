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
                curr_set = set()
                curr_set.add((i,j))
                while (not q.empty()):
                    curr = q.get()
                    for d in dir:
                        r = curr[0] + d[0]
                        c = curr[1] + d[1]
                        if r>=0 and r<m and c>=0 and c<n and matrix[r][c]== temp and ((r,c) not in visited):
                            area += 1
                            visited.add((r,c))
                            curr_set.add((r,c))
                            q.put([r, c])
                print(curr_set)
                for r,c in curr_set:
                    temp = matrix[r][c]
                    up = r-1
                    left = c-1
                    if ((up<0 or matrix[up][c]!=temp) and (left<0 or matrix[r][left]!=temp)) or ((up>=0 and matrix[up][c]==temp) and (left>=0 and matrix[r][left]==temp)):
                        if up<0 or left<0:
                            peri += 1
                        elif matrix[up][left]!=temp:
                            peri += 1
                        elif matrix[up][c]!=temp and matrix[r][left]!=temp:
                            peri+=1
                    down = r+1
                    left = c-1
                    if ((down>=m or matrix[down][c]!=temp) and (left<0 or matrix[r][left]!=temp)) or ((down<m and matrix[down][c]==temp) and (left>=0 and matrix[r][left]==temp)):
                        if down>=m or left<0:
                            peri += 1
                        elif matrix[down][left]!=temp:
                            peri += 1
                        elif matrix[down][c]!=temp and matrix[r][left]!=temp:
                            peri += 1
                    down = r+1
                    right = c+1
                    if ((down>=m or matrix[down][c]!=temp) and (right>=n or matrix[r][right]!=temp)) or ((down<m and matrix[down][c]==temp) and (right<n and matrix[r][right]==temp)):
                        if down>=m or right>=n:
                            peri += 1
                        elif matrix[down][right]!=temp:
                            peri += 1
                        elif matrix[down][c]!=temp and matrix[r][right]!=temp:
                            peri += 1
                    up = r-1
                    right = c+1
                    if ((up<0 or matrix[up][c]!=temp) and (right>=n or matrix[r][right]!=temp)) or ((up>=0 and matrix[up][c]==temp) and (right<n and matrix[r][right]==temp)):
                        if up<0 or right>=n:
                            peri += 1
                        elif matrix[up][right]!=temp:
                            peri += 1
                        elif matrix[up][c]!=temp and matrix[r][right]!=temp:
                            peri+=1
                sum += peri * area
    return sum

path = "/Users/smituplenchwar/Documents/AOC2024/12/advcode12.txt"

matrix = read_input(path)

print(fence(matrix))



