from functools import cache

def read_input(path):
    with open(path, "r") as file:
        for line in file:
            row = [int(x) for x in line.strip().split(" ")]
    return row

@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps-1)
    s = str(stone)
    n = len(s)
    if n % 2 == 0:
        s1 = int(s[:n//2])
        s2 = int(s[n//2:])
        return count(s1, steps-1) + count(s2, steps-1)
    else:
        return count(stone*2024, steps-1)      

def stones(arr):
    sum1 = 0
    for num in arr:
        sum1 += count(num, 75)
    return sum1

path = "/Users/smituplenchwar/Documents/AOC2024/11/advcode11.txt"
arr = read_input(path)

sum = stones(arr)

print(sum)