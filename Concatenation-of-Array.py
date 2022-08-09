# 1929. Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]

# Solution 1
def getConcatenation(nums):
    s = []
    for i in range (len(nums)):
        s.append(nums[i])
    for i in range (len(nums)):
        s.append(nums[i])
    return s

# Solution 2
def getConcatenation(nums):
    s = len(nums)*2*[0]
    for i in range (len(nums)):
        s[i] = nums[i]
        s[i+len(nums)] = nums[i]
    return s

