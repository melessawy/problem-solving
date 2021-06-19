#string compression problem
#Run Length Encoding

#Given an input string of a certain length, design an algorithm that compresses the string. 
#The string should be compressed such that consecutive duplicates of characters are replaced 
#with the character and followed by the number of consecutive duplicates.

#For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3dex6”.

def compressedString(message):
    x = 0
    combined = ""
    length=len(message)
    while (x != length):
        count = 1

        while ((x < (length-1)) and (message[x] == message[x+1])):
            count = count + 1
            x = x + 1

        if (count == 1):
            combined = combined + str(message[x])
        else:
            combined = combined + str(message[x]) + str(count)

        x = x + 1

    print (combined)


# test 
message = "wwwwaaadexxxxxx"
compressedString(message)
message = "abaabbbc"
compressedString(message)
