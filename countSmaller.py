#315. Count of Smaller Numbers After Self
#You are given an integer array nums and you have to return 
#a new counts array. The counts array has the property where 
#counts[i] is the number of smaller elements to the right of nums[i].

#example input
# nums = [5,2,6,1] => [2,1,1,0]
# nums = [-1]  => [0]
# nums = [-1,-1]  => [0,0]


#-------------------------------------------------------------------------------

#Traditional looping solution - doesn't meet Leetcode time requirements

def countSmaller(nums):
    
    #initiate an empty list for final solution
    count_array=[]

    #extract the list of numbers on the right of our number of interest
    for i in range(len(nums)):
        index_from = i+1
        index_to = len(nums)
        right_list = nums[index_from:index_to]

        #count the numbers in right_list that are smaller than our number
        counter=0

        for x in right_list:
            if x<nums[i]: 
                counter=counter+1

        #insert the counted result into our solution array
        count_array.insert(len(count_array)+1, counter)

    print(count_array)

    
#-------------------------------------------------------------------------------

#binary search attempt - doesn't meet Leetcode time requirements

# full answer with binary search
# doesn't pass leetcode's time limit


def countSmaller(nums):
    
    def binary_search(nums, low_ind, high_ind, x):

        # Check base case
        if high_ind==low_ind and nums[low_ind]<x:
            return(low_ind)
        if high_ind==low_ind and nums[low_ind]>=x:
            if low_ind==0: return(-1)
            elif low_ind>0 and nums[low_ind]>=x: return(low_ind-1)
            elif low_ind>0 and nums[low_ind]<x: return(low_ind)

        if high_ind > low_ind:

            mid = (high_ind + low_ind) // 2

            # if mid =0
            if mid==0:
                if nums[mid]>=x: return(-1)
                if nums[mid]<x and nums[mid+1]<x: return(mid+1)
                if nums[mid]<x and nums[mid+1]>=x: return(mid)

            # If element is present at the middle itself
            if nums[mid] == x:
                return (mid-1)

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif nums[mid] > x and nums[mid-1] >= x:
                return binary_search(nums, low_ind, mid - 1, x)
            elif nums[mid] > x and nums[mid-1] < x:
                return (mid-1)

            # Else the element can only be present in right subarray
            elif nums[mid] < x and nums[mid+1] <= x:
                return binary_search(nums, mid + 1, high_ind, x)

            elif nums[mid] < x and nums[mid+1] > x:
                return (mid)
        # end of binnary search function ----------------------------
    
    #initiate an empty list for final solution
    count_array=[]
    
    #extract the list of numbers on the right of our number of interest
    for i in range(len(nums)):
        
        if i==len(nums)-1:
            count_array.append(0)
            break

        else:
            index_from = i+1
            index_to = len(nums)
            right_list = nums[index_from:index_to]

            x=nums[i]
            right_list.sort()
            low_ind = 0
            high_ind = len(right_list)-1

            index=binary_search(right_list, low_ind, high_ind, x)
            
            if index==-1:
                count_array.append(0)
            else:            
                count = index + 1
                count_array.append(count)

    return (count_array)


#-------------------------------------------------------------------------------

# This solution works fine with leetcode's long testcases
# I basically read the integers one by one (from the right side) 
# into a stack. After every insertion into the stack, I would 
# compare the stack to the number that was on the left of the 
# last number I inserted into my stack.

# to read the list from right to left, I used [::-1] to
# basically flip the list items around!

# Using bisect, I could return a proposed index for each number, 
# that would make my stack sorted. If you think about it, if 
# a number needs to be in index 2 for the stack to be sorted, 
# that means that my number had 2 other smaller numbers to the 
# right of it. So basically all I needed is to return that 
# index for every number.

def countSmaller(nums):
    
    import bisect
    
    stack = []
    final_list = []

    for number in nums[::-1]:
        index = bisect.bisect_left(stack, number)
        final_list.append(index)
        stack.insert(index, number)
        
    return(final_list[::-1])
