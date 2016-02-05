def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char in 'aeiouAEIOU':
        return True
    else:
        return False
        
    #Could also use:
    #return char.lower() in 'aeiou'
