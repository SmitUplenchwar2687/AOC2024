def isSafe(nums):
    if len(nums) < 2:
        return True
    count1 = 0
    count2 = 0 
    for i in range(len(nums)-1):
        temp = nums[i] - nums[i+1]
        if count1 > 2:
            return False 
        
        elif  temp < 1 or temp > 3:
            count1 += 1
            if i < len(nums)-1 and count1 == 1 and (nums[i]-nums[i+2])      
        else:
            count2 += 1
    if count2>= len(nums)-2:
        return True
    count1 = 0
    count2 = 0
    for i in range(len(nums)-1):
        temp = nums[i+1] - nums[i]
        if count1 > 2:
            return False
        
        elif  temp < 1 or temp > 3:
             count1 += 1
        else:
            count2 += 1
    if count2>= len(nums)-2:
        return True
    else:
        return False