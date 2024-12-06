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
                print(i,j,"up")
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
                print(i,j,"right")
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
                print(i,j,"down")
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
                print(i,j,"left")
                j = j - 1
            if j<0:
                return False
            j = j + 1
            left = False
            up = True
