#Dam Design problem
#Your company is designing a dam to be built across a stream to create a small lake. 
#To reduce materials cost, it will be made of one or more concrete walls with mud 
#packed in between them. Determine the maximum height of the mud segments in the 
#dam with the following restrictions: 

#• one unit width of the gap between walls will contain one segment of packed mud 
#• the height of mud in a segment cannot exceed 1 unit more than an adjacent wall 
#  or mud segment. 

#Given the placement of a number of walls and their heights, determine the 
#maximum height of a mud segment that can be built. 
#If no mud segment can be built, return 0. 

#Example wallpositions = [1, 2, 4, 7] wallheights = [4, 6, 8, 11] 

def maxHeight(wallPositions, wallHeights):
    mud = 0    
    for i in range(len(wallPositions)-1):
        if(wallPositions[i] < wallPositions[i+1]-1):
            height = abs(wallHeights[i+1]-wallHeights[i])
            gap = wallPositions[i+1] - wallPositions[i]-1
            temp = 0
            if gap > height:
                count = max(wallHeights[i+1], wallHeights[i])+1
                gap_left = gap - height -1
                temp = count + gap_left/2
            else:
                temp = min(wallHeights[i+1], wallHeights[i])+gap
            mud = max(mud, temp)    
    return int(mud)


#Test 1
wallPositions = [1, 3, 7]
wallHeights = [4, 3, 3]

maxHeight(wallPositions, wallHeights)

#Test 2
wallPositions = [1, 2, 4, 7]
wallHeights = [4, 6, 8, 11] 

maxHeight(wallPositions, wallHeights)
