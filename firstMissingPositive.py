# 41. First Missing Positive
# Given an unsorted integer array nums, find the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# test examples
# nums = [1,2,0] => 3
# nums = [3,4,-1,1] => 2
# nums = [7,8,9,11,12] => 1
# nums = [2,2] => 1
# nums = [-2,-2] => 1
# nums = [4] => 1


def firstMissingPositive(nums):
    
    if len(nums)==1:
        if nums[0]>1 or nums[0]<=0: return(1)
        elif nums[0]==1: return(2)
    
    nums.sort()
    stack=[]
    found=0
    
    for number in nums:
        if number > 0:
            if stack!=[] and (number-stack[-1])>1:
                found=1
                if stack[0] == 1:
                    return(stack[-1]+1)
                else: return (1)
            else: stack.append(number)
        elif number <= 0: next
    if found == 0 and nums[len(nums)-1]+1 <= 0: return(1)
    elif found == 0 and stack[0] != 1: return(1)
    else: return(nums[len(nums)-1]+1)
    
    
# test examples
# nums = [1,2,0] 
# nums = [3,4,-1,1]
# nums = [7,8,9,11,12] 
# nums = [2,2]
# nums = [-2,-2] 
# nums = [4] 
firstMissingPositive(nums)
