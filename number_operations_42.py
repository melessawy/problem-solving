#number operations

#Alice has invented a new card game to play with Bob. Alice made a deck of cards with random values between 1 and 52. 
#Bob picks 5 cards. Then, he has to rearrange the cards so that by utilizing the operations plus, minus, or times, 
#the value of the cards reach Alice's favorite number. 42. More precisely find operations such that 
#((((val1 op1 val2) op2 val3) op3 val4) op4 val) = 42. Help Bob by writing a program to determine whether it is possible 
#to reach 42 given 5 card values. For example, Bob picks 5 cards out of the deck containing 40, 1, 3, 4, and 20. 
#Bob rearranges the cards and supplies four operations, so that 4 * 20 - 40 + 3 - 1 = 42. 
#Input: The input consists of five integers on a line, separated by spaces. 
#Each integer is between 1 and 52, inclusive, 
#Output: Print a line containing "YES" if it is possible to reach the value 42 according to the rules of the game, 
#or "NO" otherwise. 

#Test Input: 40 1 3 4 20 Expected Output: YES

def number_ops_not_42(line):
    import itertools
    import sys

    #Creating list of numbers
    nums=[]
    for i in line.split(" "):
        nums.append(int(i))

    #Creaing list of operations
    ops=["+", "-", "*", "+", "-", "*"]

    #function to evaluate all possible operations on each number order
    def operation(nums,ops):
        for x in nums:

            global result
            result="NO"

            for i in ops:
                op1=i[0]
                op2=i[1]
                op3=i[2]
                op4=i[3]

                chunk1=str(x[0])+op1+str(x[1])
                chunk2=str(chunk1)+op2+str(x[2])
                chunk3=str(chunk2)+op3+str(x[3])
                chunk4=str(chunk3)+op4+str(x[4])

                res=eval(chunk4)

                if res==42:
                    result="YES"
                    break

    #creating list of permutations
    numsPermutes=list(itertools.permutations(nums,5))
    opsPermutes=list(itertools.permutations(ops,4))

    #Decision
    operation(numsPermutes,opsPermutes)
    print(result)
    

# Test
line="40 1 3 4 20"
number_ops_not_42(line)

line="40 2 3 4 20"
number_ops_not_42(line)
