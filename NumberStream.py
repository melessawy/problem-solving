# Have the function NumberStream(str) take the str parameter 
# being passed which will contain the numbers 2 through 9, 
# and determine if there is a consecutive stream of digits 
# of at least N length where N is the actual digit value. 
# If so, return the string true, otherwise return the 
# string false. For example: if str is "6539923335" then 
# your program should return the string true because there 
# is a consecutive stream of 3's of length 3. The input 
# string will always contain at least one digit.

# Examples
# Input: "5556293383563665"
# Output: false
# Input: "5788888888882339999"
# Output: true

def NumberStream(strParam):
    for i in range(0, len(strParam)):
        length = 1
        for j in range (i+1, len(strParam)):
            if (strParam[i] == strParam[j]):
                length = length + 1
            elif (strParam[i] != strParam[j]):
                break
        if (length >= int(strParam[i]) and length != 0):
            return (True)
    return (False)
