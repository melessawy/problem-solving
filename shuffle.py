# 1470. Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].



def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(0,n,1):
        res.append(nums[i])
        res.append(nums[i+n])
    return(res)

# Examples
# nums = [2,5,1,3,4,7]
# n = 3
# result: [2,3,5,4,1,7]

# nums = [1,2,3,4,4,3,2,1]
# n = 4
# result: [1,4,2,3,3,2,4,1]

# nums = [1,1,2,2]
# n = 2
# result: [1,2,1,2]
