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
            x1 = num[0][0] - diffx
            y1 = num[0][1] - diffy
            if x1>=0 and x1<m and y1>=0 and y1<n:
                nodes.add((x1,y1))
            x2 = num[1][0] + diffx
            y2 = num[1][1] + diffy
            if x2>=0 and x2<m and y2>=0 and y2<n:
                nodes.add((x2,y2))
    return len(nodes)
                        
path = "/Users/smituplenchwar/Documents/AOC2024/8/advcode8.txt"
matrix = read_input(path)

ant = antenna(matrix)

ant_comb = combinations(ant)

count = antinodes(ant_comb, matrix)

print(count)
