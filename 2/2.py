def updatedisSafe(nums):
    if len(nums) < 2:
        return True
    for i in range(len(nums)):
        temp = nums.copy()
        temp.pop(i)
        if isSafe(temp):
            return True
    return False
        
def isSafe(nums):
    if len(nums) < 2:
        return True
    count = 0
    if nums[0] - nums[1] > 0:
        for i in range(len(nums)-1):
            temp = nums[i] - nums[i+1]
            if  temp < 1 or temp > 3:
                return False
    else:
        for i in range(len(nums)-1):
            temp = nums[i+1] - nums[i]
            if  temp < 1 or temp > 3:
                return False
    return True

with open('advcode2.txt', 'r') as file:
    lines = file.readlines()

numbers = []
count = 0
for i in range(len(lines)):
    numbers.append([int(num) for num in lines[i].split()])
    if updatedisSafe(numbers[i]):
        count += 1


print(len(numbers))
print(count)