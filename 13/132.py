def read_input(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            row = line.strip().split("\n")
            temp = row[0].split(" ")
            if temp != [""]:
                arr.append(temp)
    return arr

def transform_input(arr):
    n = len(arr)
    matrix = []
    for i in range(n):
        if i%3 == 0 or i%3 == 1:
            temp = arr[i]
            s1 = temp[2]
            s2 = temp[3]
            s1 = s1[:-1]
            num1 = s1.split("+")
            num2 = s2.split("+")
            matrix.append([int(num1[1]),int(num2[1])])
        else:
            temp = arr[i]
            s1 = temp[1]
            s2 = temp[2]
            s1 = s1[:-1]
            num1 = s1.split("=")
            num2 = s2.split("=")
            matrix.append([int(num1[1]),int(num2[1])])
    return matrix        
            

def tokens(arr):
    n = len(arr)
    sum = 0
    for i in range(0, n, 3):
        a1 = arr[i][0]
        a2 = arr[i][1]
        b1 = arr[i+1][0]
        b2 = arr[i+1][1]
        c1 = arr[i+2][0]+10000000000000
        c2 = arr[i+2][1]+10000000000000
        x = (b2*c1 - b1*c2)/(a1*b2 - a2*b1)
        y = (c2*a1 - c1*a2)/(a1*b2 - a2*b1)
        if x.is_integer() and y.is_integer():
            sum += 3*x + y
    return sum 
        
path = "/Users/smituplenchwar/Documents/AOC2024/13/advcode13.txt"

arr = read_input(path)

matrix = transform_input(arr)

print(tokens(matrix))