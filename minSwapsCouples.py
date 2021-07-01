# 765. Couples Holding Hands
# There are n couples sitting in 2n seats arranged in a row and 
# want to hold hands. The people and seats are represented by an 
# integer array row where row[i] is the ID of the person sitting 
# in the ith seat. The couples are numbered in order, the first 
# couple being (0, 1), the second couple being (2, 3), and so on 
# with the last couple being (2n - 2, 2n - 1).

# Return the minimum number of swaps so that every couple is 
# sitting side by side. A swap consists of choosing any two 
# people, then they stand up and switch seats.

# test examples
# Input: row = [0,2,1,3]
# Output: 1
# Input: row = [3,2,0,1]
# Output: 0

#-----------------------------------------------------------

def minSwapsCouples(row):
    
    moves = 0 #counter for the number of moves
    
    for x in range(0,len(row)-1,2): # a loop to check every 2 neighbours to see if they can form a couple
        
        if(row[x]%2==0): # if the remainder of division =0, then this would be the even member, so add one to get their couple (odd number)
            temp = row[x]+1
        else:
            temp = row[x]-1 # as the remainder of division !=0, we know that this is an member, so subtract one to get their couple (even number)
            
        if temp == row[x+1]: # test the neighbour to see if it's the correct couple
            continue #yes, correct couple. continue with to the next couple
            
        else: # not a correct couple
            for y in range(x+2,len(row),1): # check every number to find the right couple
                if row[y]==temp: 
                    row[x+1],row[y] = row[y],row[x+1] # once found, switch locations with the wrong couple
                    moves=moves+1 # add 1 to the moves counter
                    break
                
    return (moves)


#-----------------------------------------------------------
#Test examples
row = [3,2,0,1]
row = [0,2,1,3]
minSwapsCouples(row)
