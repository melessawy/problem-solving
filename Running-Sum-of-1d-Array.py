# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

def runningSum(nums):
    result=[]
    temp=0
    for i in range (0, len(nums)):
        if i == 0:
            temp = nums[0]
        if i > 0:
            for i in range(0, i+1):
                temp = temp + nums[i]
        result.append(temp)
        temp=0
    return(result)

#test
nums = [3,1,2,10,1]
runningSum(nums)
