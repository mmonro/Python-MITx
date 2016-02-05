def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a
        
    gcd = start
    
    while gcd > 0:
        if (start % gcd == 0) and (end % gcd == 0):
            return gcd
        gcd -= 1 
        
    return gcd

print gcdIter(6, 12)
