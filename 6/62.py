def guard_start(matrix):
    m  = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "^":
                return [i,j]


def guard_loop(matrxi, start):
    m  = len(matrix)
    n = len(matrix[0])
    count = 0
    flag = False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "#" or matrix[i][j] == "^":
                continue
            else:
                temp = matrix.copy()
                temp[i][j] = "#"
                flag = guard_steps(temp, start)
                if flag:
                    count = count + 1
    return count
                



def guard_steps(matrix, start):
    m  = len(matrix)
    n = len(matrix[0])
    visited = set()
    up = True
    down = False
    right = False
    left = False
    i = start[0]
    j = start[1]
    while(True):
        if up:
            while (i>=0 and matrix[i][j]!="#"):
                if (i,j,"up") not in visited:
                    visited.add((i,j,"up"))
                elif (i,j,"up") in visited and matrix[i][j]!="#":
                    return True
                i = i - 1
            if i<0:
                break
            i = i + 1
            up = False
            right = True
        
        elif right:
            while (j<n and matrix[i][j]!="#"):
                if (i,j,"right") not in visited:
                    visited.add((i,j,"right"))
                elif (i,j,"right") in visited and matrix[i][j]!="#":
                    return True
                j = j + 1       
            if j>=n:
                break
            j = j - 1
            right = False
            down = True
        
        elif down:
            while (i<m and matrix[i][j]!="#"):
                if (i,j,"down") not in visited:
                    visited.add((i,j,"down"))
                elif (i,j,"down") in visited and matrix[i][j]!="#":
                    return True
                i = i + 1
            if i>=m:
                break
            i = i - 1
            down = False
            left = True
        
        elif left:
            while (j>=0 and matrix[i][j]!="#"):
                if (i,j,"left") not in visited:
                    visited.add((i,j,"left"))
                elif (i,j,"left") in visited and matrix[i][j]!="#":
                    return True
                j = j - 1
            if j<0:
                break
            j = j + 1
            left = False
            up = True
    return False
            

def read_input_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

file_path = "/Users/smituplenchwar/Documents/AOC2024/6/test.txt"  
matrix = read_input_from_file(file_path)


start = guard_start(matrix)

print(guard_loop(matrix, start))