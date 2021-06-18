# Multiply 2 Lists of numbers. Both lists should have equal number of items.
# The lists are to be read as one string, with spaces separating numbers and the character | separating the two lists
# Example: line = "9 0 6 | 15 14 9"

def multiply_2_lists(line):
    #Creating a list of items
    line=line.split()

    list1=[]
    list2=[]

    #Creating list#1
    for num in line:
        if num!="|":
            list1.append(int(num))
        if num=="|":
            delim_index=line.index("|")
            break

    #Creating list#2
    for i in range(delim_index+1,len(line)):
        list2.append(int(line[i]))

    #multiplication
    multiplied=[]

    for x in range(len(list1)):
        multiplied.append(list1[x]*list2[x])

    #Creating list of strings
    multiplied2=[]
    for z in range(len(multiplied)):
        multiplied2.append(str(multiplied[z]))

    #creating final line
    space=" "
    line2=space.join(multiplied2)
    return(line2)

#----------------------------------------------

#Example

line = "9 0 6 | 15 14 9"
multiply_2_lists(line)
