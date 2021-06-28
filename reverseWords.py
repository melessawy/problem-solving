# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within 
# a sentence while still preserving whitespace and initial word order.

#Examples
# Input: s = "Let's take LeetCode contest"
# Input: s = "God Ding"

def reverseWords(s: str) -> str:
    
    list=s.split(" ")
    list2=[]
    
    for word in list:
        word=word[::-1]
        list2.append(word)
    
    s=" ".join(list2)
    
    return(s)

# test example
s = "God Ding"
reverseWords(s)
