def order_map(order):
    mapping = {}
    for i in order:
        if i[1] in mapping:
            mapping[i[1]].append(i[0])
        else:
            mapping[i[1]] = [i[0]]
    return mapping

class ordering:
    def updated_order(self, arr1, maps):
        self.map = maps.copy()
        self.res = []
        self.rest = set()
        self.arr = set()
        for i in arr1:
            self.arr.add(i)
        for num in arr1:
            self.helper(num)
        return self.res
   
    def helper(self, temp):
        if temp in self.rest:
            return
        if temp not in self.map:
            if temp in self.arr:
                self.res.append(temp)
                self.rest.add(temp)
            return
        
        for num in self.map[temp]:
            if num in self.arr:
                self.helper(num)
        
        if temp in self.arr and temp not in self.rest:
            self.res.append(temp)
            self.rest.add(temp)


def read_order_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip().split("|"))
            row[0] = int(row[0])
            row[1] = int(row[1])
            matrix.append(row)
    return matrix

def read_input_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip().split(","))
            row = [int(num) for num in row]
            matrix.append(row)
    return matrix

file_path = "/Users/smituplenchwar/Documents/AOC2024/5/advcode5.txt"  
order = read_order_from_file(file_path)

file_path_1 = "/Users/smituplenchwar/Documents/AOC2024/5/advcode5_2.txt"  
matrix_1 = read_input_from_file(file_path_1)


maps = order_map(order)

result = 0

for num in matrix_1:
    order_1 = ordering()
    temp = order_1.updated_order(num, maps)
    print(temp)
    flag = True
    for i in range(len(num)):
        if num[i] != temp[i]:
            flag = False
            break
    mid = (len(num)//2)
    if flag == False:
        print(temp[mid])
        result += temp[mid]

print(result)
