import copy

def guard_start(matrix):
    m  = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "^":
                return [i,j]


def guard_steps_visit(matrix, start):
    m  = len(matrix)
    n = len(matrix[0])
    visited = set()
    count = 0
    up = True
    down = False
    right = False
    left = False
    i = start[0]
    j = start[1]
    while(True):
        if up:
            while (i>=0 and matrix[i][j]!="#"):
                if (i,j) not in visited:
                    visited.add((i,j))
                    count = count + 1
                i = i - 1
            if i<0:
                break
            i = i + 1
            up = False
            right = True
        
        elif right:
            while (j<n and matrix[i][j]!="#"):
                if (i,j) not in visited:
                    visited.add((i,j))
                    count = count + 1
                j = j + 1       
            if j>=n:
                break
            j = j - 1
            right = False
            down = True
        
        elif down:
            while (i<m and matrix[i][j]!="#"):
                if (i,j) not in visited:
                    visited.add((i,j))
                    count = count + 1
                i = i + 1
            if i>=m:
                break
            i = i - 1
            down = False
            left = True
        
        elif left:
            while (j>=0 and matrix[i][j]!="#"):
                if (i,j) not in visited:
                    visited.add((i,j))
                    count = count + 1
                j = j - 1
            if j<0:
                break
            j = j + 1
            left = False
            up = True
    return count, visited


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
                if (i,j,"up") in visited:
                    return True
                visited.add((i,j,"up"))
                #print(i,j,"up")
                i = i - 1
            if i<0:
                return False
            i = i + 1
            up = False
            right = True
        
        elif right:
            while (j<n and matrix[i][j]!="#"):
                if (i,j,"right") in visited:
                    return True
                visited.add((i,j,"right"))
                #print(i,j,"right")
                j = j + 1       
            if j>=n:
                return False
            j = j - 1
            right = False
            down = True
        
        elif down:
            while (i<m and matrix[i][j]!="#"):
                if (i,j,"down") in visited:
                    return True
                visited.add((i,j,"down"))
                #print(i,j,"down")
                i = i + 1
            if i>=m:
                return False
            i = i - 1
            down = False
            left = True
        
        elif left:
            while (j>=0 and matrix[i][j]!="#"):
                if (i,j,"left") in visited:
                    return True
                visited.add((i,j,"left"))
                #print(i,j,"left")
                j = j - 1
            if j<0:
                return False
            j = j + 1
            left = False
            up = True
            


def guard_loop(matrix, start):
    m  = len(matrix)
    n = len(matrix[0])
    count = 0
    flag = False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "#" or matrix[i][j] == "^":
                continue
            else:
                temp = copy.deepcopy(matrix)
                temp[i][j] = "#"
                flag = guard_steps(temp, start)
                if flag:
                    print(temp)
                    count = count + 1
    return count



def read_input_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

file_path = "/Users/smituplenchwar/Documents/AOC2024/6/advcode6.txt"  
matrix = read_input_from_file(file_path)


start = guard_start(matrix)

print(guard_loop(matrix, start))



