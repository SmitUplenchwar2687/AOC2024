def read_input(path):
    with open(path, "r") as file:
        for line in file:
            row = [int(x) for x in line.strip().split(" ")]
    return row

map = {}

def count(stone, steps):
    key = (stone, steps)
    
    if key in map:
        return map[key]
    
    if steps == 0:
        res = 1
    elif stone == 0:
        res = count(1, steps-1)
    else: 
        s = str(stone)
        n = len(s)
        if n % 2 == 0:
            s1 = int(s[:n//2])
            s2 = int(s[n//2:])
            res = count(s1, steps-1) + count(s2, steps-1)
        else:
            res = count(stone*2024, steps-1)
    
    map[key] = res
    return res
          
def stones(arr):
    sum1 = 0
    for num in arr:
        sum1 += count(num, 75)
    return sum1

path = "/Users/smituplenchwar/Documents/AOC2024/11/advcode11.txt"
arr = read_input(path)

sum = stones(arr)

print(sum)