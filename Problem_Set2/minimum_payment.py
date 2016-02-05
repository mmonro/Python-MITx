balance = 3926
annualInterestRate = .2

minPayment = 0
monthlyInterestRate = (annualInterestRate / 12)
testBalance = balance

while testBalance > 0:
    minPayment += .01
    month = 0
    testBalance = balance
    
    while month < 12:
        month += 1
        newBalance = (testBalance - minPayment)
        testBalance = newBalance + round(monthlyInterestRate * newBalance, 2)
        
    print str(testBalance) + ' ' + str(minPayment)
                            
print ('Loweset Payment: ' + str(minPayment))
