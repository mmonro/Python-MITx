low=0
high=100
status='x'
guess=0

print ('Please think of a number between 0 and 100!  ')

while status != "c":
    guess = (low + high) / 2
    print 'Is your secret number',
    print int(guess),
    print '?'
    status = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if status == "h":
        high = guess
    elif status == "l":
        low = guess    
    elif status == "c":
        break
    else:
        print ("Sorry, I did not understand your input.")

print ("Game over. Your secret number was:"),
print int(guess)
