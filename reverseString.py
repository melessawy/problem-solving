#Leetcode 344. Reverse String
#Write a function that reverses a string. The input string is given as an array of characters s
# Examples:
# Input: s = ["h","e","l","l","o"]
# Input: s = ["H","a","n","n","a","h"]

# Follow up: Do not allocate extra space for another array. You must do this by modifying 
#the input array in-place with O(1) extra memory.


def reverseString(s: list):
    len2=len(s)
    for i in range(len2):
        s.insert(i,s.pop())
    return(s)
  

#test
s = ["h","e","l","l","o"]
reverseString(s)

s = ["H","a","n","n","a","h"]
reverseString(s)
