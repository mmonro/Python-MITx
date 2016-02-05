balance = 999999
annualInterestRate = .18

monthlyInterestRate = (annualInterestRate / 12)
testBalance = balance
lowBound = round(balance / 12, 2)
highBound = round((balance * (1 + monthlyInterestRate)**12)/12, 2)
epsilon = .09
minPayment = round((lowBound + highBound) / 2, 2)

while abs(testBalance) > epsilon:
    month = 0
    testBalance = balance
    
    while month < 12:
        month += 1
        newBalance = (testBalance - minPayment)
        testBalance = newBalance + round(monthlyInterestRate * newBalance, 2)
        
    if testBalance < 0:
        highBound = minPayment
        minPayment = round((lowBound + minPayment) / 2, 2)
    elif testBalance > 0:
        lowBound = minPayment
        minPayment = round((minPayment + highBound) / 2, 2)
    else:
        break
                                                  
print ('Loweset Payment: ' + str(minPayment))
