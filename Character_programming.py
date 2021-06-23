# Character programming
# A control device has 4 buttons that can be used to move a character around 
# a screen in 4 directions: Up (U), Down (D), Left (L), and Right (R). 
# The movement needs to be optimized by deleting unnecessary instructions 
# while maintaining the same destination. 
# Given the original set of instructions, what is the maximum number 
# that can be deleted and still have the character reach the destination? 

# Note: The instructions that are deleted do not need to be contiguous. 

# Example S = 'URDR' 
# In this example, the maximum number of steps would be 2 (right, right), 
# because the steps 1 and 3 (up, down) are considered unnecessary because 
# they cancel each other

def getMaxDeletions(s):

    length = len(s)

    r = s.count('R')
    l = s.count('L')
    u = s.count('U')
    d = s.count('D')

    moves= length - (abs(u-d) + abs(r-l))
    return(moves)

#Testing
# getMaxDeletions('URDR')
# getMaxDeletions('RUDRL')
# getMaxDeletions('RRR')
# getMaxDeletions('RURUR')
