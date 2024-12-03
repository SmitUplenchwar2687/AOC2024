arr1 = []
arr2 = []
dic = {}
while(True):
    temp1, temp2 = map(int, input().split())
    if temp1 == -1:
        break
    if temp2 in dic:
        dic[temp2] += 1
    else:
        dic[temp2] = 1
        
    arr1.append(temp1)
    arr2.append(temp2)


#dic = {}
# for i in range(len(arr2)):
#     if arr2[i] in dic:
#         dic[arr2[i]] += 1
#     else:
#         dic[arr2[i]] = 1

sim = 0
for i in range(len(arr1)):
    if arr1[i] in dic:
        sim += arr1[i] * dic[arr1[i]]

print(sim)
        

# print(len(arr1))
# print(len(arr2))

# arr1.sort()
# arr2.sort()
# dist = 0
# for i in range(len(arr1)):
#     dist += abs(arr1[i] - arr2[i])
    
# print(dist)