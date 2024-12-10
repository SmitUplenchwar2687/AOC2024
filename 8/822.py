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
            
def antinodes(ant_comb, matrix, ant):
    m = len(matrix)
    n = len(matrix[0])
    nodes = set()
    
    for freq, pos in ant.items():
        if len(pos) > 1:
            nodes.update((x, y) for x, y in pos)
            
    for ant in ant_comb:
        for num in ant:
            x1, y1 = num[0]
            x2, y2 = num[1]
            diffx = x2 - x1
            diffy = y2 - y1
            if diffx != 0 and diffy != 0:
                for i in range(m):
                    for j in range(n):
                        if min(x1, x2) < i < max(x1, x2) and min(y1, y2) < j < max(y1, y2):
                            continue
                        numo = y1 - j
                        deno = x1 - i
                        if deno == 0 or diffx == 0: 
                            continue
                        if (numo * diffx) == (deno * diffy):
                            nodes.add((i, j))
            elif diffx == 0:
                for j in range(n):
                    if j < min(y1, y2) or j > max(y1, y2):  
                        nodes.add((x1, j))
            elif diffy == 0:
                for i in range(m):
                    if i < min(x1, x2) or i > max(x1, x2): 
                        nodes.add((i, y1))
                                               
    return len(nodes)
            
                        
path = "/Users/smituplenchwar/Documents/AOC2024/8/advcode8.txt"
matrix = read_input(path)

ant = antenna(matrix)

ant_comb = combinations(ant)

count = antinodes(ant_comb, matrix, ant)

print(count)
