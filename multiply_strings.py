#Given two non-negative integers num1 and num2 represented as strings, 
#return the product of num1 and num2, also represented as a string.

def multiply(num1: str, num2: str) -> str:
    num1=int(num1)
    num2=int(num2)
    m=num1*num2
    return(str(m))


#test
multiply(2,3)
multiply(123,456)
