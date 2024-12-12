def read_input(path):
    with open(path, "r") as file:
        for line in file:
            row = [int(x) for x in line.strip().split(" ")]
    return row


def digits(num):
    count = 0
    while(num != 0):
        num = num // 10
        count += 1
    return count

def blink(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr[i] = 1
            i += 1
        elif digits(arr[i]) % 2 == 0:
            digit = digits(arr[i])
            s = str(arr[i])
            s1 = s[:digit//2]
            s2 = s[digit//2:]
            arr[i] = int(s2)
            arr.insert(i, int(s1))
            i += 2
        else:
            arr[i] = arr[i]*2024
            i += 1
    return arr
                
def stones(arr):
    for i in range(75):
        arr = blink(arr)
        print(i)
    return len(arr)        

path = "/Users/smituplenchwar/Documents/AOC2024/11/test.txt"
arr = read_input(path)

newarr = stones(arr)

print(newarr)