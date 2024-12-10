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
    i = len(arr)-1
    while(i>0):
        low = 0
        if arr[i] != ".":
            temp = arr[i]
            count = 0
            while (arr[i]==temp):
                count += 1
                i -= 1
            free = 0
            while low <= i:
                if free == count:
                    break
                elif arr[low] == ".":
                    free += 1
                    low += 1
                else:
                    free = 0
                    low += 1
            if free == count:
                low = low - count
                i += count
                for j in range(count):
                    arr[low], arr[i] = arr[i], arr[low]
                    low += 1
                    i -= 1
        else:
            i -= 1
    return arr
                    
def checksum(arr):
    sum = 0
    id = 0 
    for i in range(len(arr)):
        if arr[i] != ".":
            temp = int(arr[i])
            sum += id*temp
            id += 1
        else:
            id += 1
    return sum

path = "/Users/smituplenchwar/Documents/AOC2024/9/advcode9.txt"
arr = read_input(path)

narr = tranform_input(arr)

newarr = filesystem(narr)


print(checksum(newarr))