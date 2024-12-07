def isoperation(matrix):
    count = 0
    for row in matrix:
        target = row[0]
        arr = row[1]
        flag = helper(arr, target, 0, arr[0])
        if flag:
            count += target
    return count

def helper(arr, target, i, curr):
    if i == len(arr)-1 and curr==target:
        return True
    
    if i >=len(arr)-1 or curr > target:
        return False

    return helper(arr, target, i+1, curr + arr[i+1]) or helper(arr, target, i+1, curr * arr[i+1]) or helper(arr, target, i+1, int(str(curr) + str(arr[i + 1])))
    
    
def read_input(path):
    doc = []
    with open(path, "r") as file:
        for line in file:
            row = list(line.strip().split(":"))
            row[0] = int(row[0])
            row[1] = row[1].strip().split(" ")
            row[1] = [int(num) for num in row[1]]
            doc.append(row)
    return doc

path = "/Users/smituplenchwar/Documents/AOC2024/7/advcode7.txt"
matrix = read_input(path)

#print(matrix)

print(isoperation(matrix))
