def read_input(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr = list(line.strip())
    return arr

def tranform_input(arr):
    narr = []
    file = 0
    for i in range(len(arr)):
        temp = int(arr[i])
        if i%2 == 0:
            for j in range(temp):
                narr.append(file)
            file += 1
        else:
            for j in range(temp):
                narr.append(".")
    return narr
            
def filesystem(arr):
    low = 0
    high = len(arr)-1
    while(low<=high):
        if arr[low]!=".":
            low += 1
        elif arr[high]==".":
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    return arr

def checksum(arr):
    sum = 0
    id = 0 
    for i in range(len(arr)):
        if arr[i] != ".":
            temp = int(arr[i])
            sum += id*temp
            id += 1
    return sum

path = "/Users/smituplenchwar/Documents/AOC2024/9/advcode9.txt"
arr = read_input(path)

narr = tranform_input(arr)

nearr = filesystem(narr)

print(checksum(nearr))