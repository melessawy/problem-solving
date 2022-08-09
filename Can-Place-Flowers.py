# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

def canPlaceFlowers(flowerbed, n):
    avail = 0
    for i in range(len(flowerbed)):
        if (len(flowerbed) == 1 and flowerbed[i]==0) or (i != len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0) or (i == 0 and flowerbed[i]==0 and flowerbed[i+1]==0) or (i == len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0):
            avail = avail +1
            flowerbed[i]=1
    if avail >= n:
        return True
    else: return False
    
#tests
flowerbed = [1,0,0,0,1]
n = 2
canPlaceFlowers(flowerbed, n)

flowerbed = [0,0,1,0,1]
n = 1
canPlaceFlowers(flowerbed, n)

flowerbed = [1,0,1,0,0]
n = 1
canPlaceFlowers(flowerbed, n)

flowerbed = [0]
n = 1
canPlaceFlowers(flowerbed, n)
