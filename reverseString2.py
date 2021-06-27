#541. Reverse String II
#Given a string s and an integer k, reverse the first k characters 
#for every 2k characters counting from the start of the string.

#If there are fewer than k characters left, reverse all of them. 
#If there are less than 2k but greater than or equal to k characters, 
#then reverse the first k characters and left the other as original.

#Examples
# Input: s = "abcdefg", k = 2
# Input: s = "abcd", k = 2

def reverseString(s: str, k: int):
    char_list = list(s)
    for s in range(0, len(s), 2*k):
        char_list[s:s+k] = char_list[s:s+k][::-1]
    final_s="".join(char_list)
    return(final_s)
  
#Test
s = "abcdefg"
k=2
reverseString(s,k)

s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
k = 39
reverseString(s,k)

