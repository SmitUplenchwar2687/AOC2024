def read_input(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            row = line.strip().split(" ")
            arr.append(row)
    return arr

def transform_input(arr):
    n = len(arr)
    arr1 = []
    for i in range(n):
        s1 = arr[i][0]
        s2 = arr[i][1]
        s1 = s1.split("=")
        s1 = s1[1]
        s1 = s1.split(",")
        s1[0] = int(s1[0])
        s1[1] = int(s1[1])
        s2 = s2.split("=")
        s2 = s2[1]
        s2 = s2.split(",")
        s2[0] = int(s2[0])
        s2[1] = int(s2[1])
        arr1.append(s1)
        arr1.append(s2)
    return arr1

def robots(arr):
    m = 103
    n = 101
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    n1 = len(arr)
    for i in range(0, n1, 2):
        p = arr[i]
        v = arr[i+1]
        for j in range(100):
            p[0] = (p[0]+v[0]) % n
            p[1] = (p[1]+v[1]) % m
        if p[0]<n//2 and p[1]<m//2:
            q1 += 1
        elif p[0]>n//2 and p[1]<m//2:
            q2 += 1
        elif p[0]>n//2 and p[1]>m//2:
            q3 += 1
        elif p[0]<n//2 and p[1]>m//2:
            q4 += 1
    return q1*q2*q3*q4

path = "/Users/smituplenchwar/Documents/AOC2024/14/advcode14.txt"

arr = read_input(path)

newarr = transform_input(arr)


print(robots(newarr))