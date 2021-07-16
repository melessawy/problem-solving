#write a function that calculates power operation, given the base number and the exponent

def power(base, exponent):
    
    #initiate result
    result=base
    
    #zero power handler
    if exponent==0: return(1)
    
    #negative power handler
    if exponent<0: temp_ex=exponent*(-1)
    else: temp_ex=exponent
    
    #calculation
    for i in range(0,temp_ex-1):
        result=result*base
    
    #return the result, or 1/result in case of negative power
    if exponent<0: return(1/result)
    else: return(result)
    
#---------------------------------------------------------------------
#test cases
power(2,1)
power(2,0)
power(2,3)
power(-2,1)
power(-2,2)
power(-2,3)
power(-2,-2)
power(2,-2)
