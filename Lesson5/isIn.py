def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    elif len(aStr) == 1:
        if aStr == char:
            return True
        else:
            return False
    else:
        midStr = aStr[(len(aStr)/2)]
        if midStr == char:
            return True
        elif midStr > char:
            return isIn(char, aStr[:len(aStr)/2])
        else:
            return isIn(char, aStr[len(aStr)/2:])
        
print isIn('e', 'fghijklm')
