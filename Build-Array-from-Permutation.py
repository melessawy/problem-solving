# 1920. Build Array from Permutation
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

# Example 1:
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]

# Example 2:
# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]

def buildArray(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans

# Example
nums = [0,2,1,5,3,4]
buildArray(nums)

# Example
nums = [5,0,1,2,3,4]
buildArray(nums)
