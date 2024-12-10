def read_input(path):
    matrix = []
    with open(path, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix


def antenna(matrix):
    ant = {}
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j]!= ".":
                if matrix[i][j] in ant:
                    ant[matrix[i][j]].append([i,j])
                else:
                    ant[matrix[i][j]] = []
                    ant[matrix[i][j]].append([i,j])
    return ant

def combinations(ant):
    ant_comb = []
    for num in ant:
        comb = []
        arr = ant[num]
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                comb.append([arr[i],arr[j]])
        ant_comb.append(comb)
    return ant_comb
            
def antinodes(ant_comb, matrix):
    m = len(matrix)
    n = len(matrix[0])
    nodes = set()
    for ant in ant_comb:
        for num in ant:
            diffx = num[1][0] - num[0][0]
            diffy = num[1][1] - num[0][1]
            if (diffx > 0 and diffy > 0) or (diffx < 0 and diffy < 0):
                for i in range(0, min(num[0][0],num[1][0])):
                    for j in range(max(num[0][1],num[1][1]), n):
                        numo = num[0][1] - j
                        deno = num[0][0] - i
                        s1 = numo/deno
                        s2 = diffy/diffx
                        if s1 == s2 and ((i,j) not in nodes):
                            nodes.add((i,j))
                for i in range(max(num[0][0],num[1][0]), m):
                    for j in range(0, min(num[0][1],num[1][1])):
                        numo = num[0][1] - j
                        deno = num[0][0] - i
                        s1 = numo/deno
                        s2 = diffy/diffx
                        if s1 == s2 and ((i,j) not in nodes):
                            nodes.add((i,j))
            if (diffx > 0 and diffy < 0) or (diffx < 0 and diffy > 0):
                for i in range(0, min(num[0][0],num[1][0])):
                    for j in range(0, min(num[0][1],num[1][1])):
                        numo = num[0][1] - j
                        deno = num[0][0] - i
                        s1 = numo/deno
                        s2 = diffy/diffx
                        if s1 == s2 and ((i,j) not in nodes):
                            nodes.add((i,j))
                for i in range(max(num[0][0],num[1][0]), m):
                    for j in range(max(num[0][1],num[1][1]), n):
                        numo = num[0][1] - j
                        deno = num[0][0] - i
                        s1 = numo/deno
                        s2 = diffy/diffx
                        if s1 == s2 and ((i,j) not in nodes):
                            nodes.add((i,j))
            if diffx == 0:
                for j in range(min(num[0][1],num[1][1])):
                    if (num[0][0], j) not in nodes:
                        nodes.add((num[0][0], j))
                for j in range(max(num[0][1],num[1][1]), n):
                    if (num[0][0], j) not in nodes:
                        nodes.add((num[0][0], j))
            if diffy == 0:
                for i in range(min(num[0][0],num[1][0])):
                    if (i, num[0][1]) not in nodes:
                        nodes.add((i, num[0][1]))
                for i in range(max(num[0][0],num[1][0]), m):
                    if (i, num[0][1]) not in nodes:
                        nodes.add((i, num[0][1]))           
                              
    return len(nodes)
            
                        
path = "/Users/smituplenchwar/Documents/AOC2024/8/test.txt"
matrix = read_input(path)

ant = antenna(matrix)

ant_comb = combinations(ant)

count = antinodes(ant_comb, matrix)

print(count)
