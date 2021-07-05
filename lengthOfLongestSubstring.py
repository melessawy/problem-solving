# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring without repeating characters.

# Examples:
# Input: s = "abcabcbb"
# Output: 3
# Input: s = "bbbbb"
# Output: 1
# Input: s = "pwwkew"
# Output: 3
# Notice that the answer must be a substring,
# "pwke" is a subsequence and not a substring.
# Input: s = ""
# Output: 0


def lengthOfLongestSubstring(s: str):
    
    #I will feed the string characters one by one to a stack 
    #to track repeating characters
    
    #function to check if a letter exists in the stack
    def findLetter(stack, letter):
        if letter not in stack:
            return False
        return True
    
    #initiating lists and variables
    stack=[]
    maxCounts=[]
    counter=0
    
    #main loop
    for letterIndex in range(len(s)):
        
        #if the letter is not in the stack, add it
        if stack==[] or findLetter(stack, s[letterIndex])==False:
            stack.append(s[letterIndex])
            counter=counter+1
        
        #if the letter was previously added to the stack:
        elif findLetter(stack, s[letterIndex]):
            ind=stack.index(s[letterIndex]) #find the index of that letter in the stack
            
            #drop the letter from the stack (and if its not in the top of the stack, 
            #drop the chunk from the top of the stack upto it)
            #example: stack = [d,f,g,h] letter=f, stack after deletion=[g,h]
            del stack[0:ind+1] 
            
            maxCounts.append(counter) #add the current counter to maxCounts
            stack.append(s[letterIndex]) #add the current letter to the end of the stack
            counter=len(stack) #reset the counter

    maxCounts.append(counter) #add counter for cases where the last chunk has no repetition

    if counter==len(s):
        return(counter) #in case the string has no repeated chars, return counter
    else:
        return(max(maxCounts)) #else, return the biggest counter in maxCounts
      
      
#===============================

#Exampe
s="pwwkew"
lengthOfLongestSubstring(s)
