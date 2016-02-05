balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

month = 0
totalPaid = 0.0
monthlyInterestRate = (annualInterestRate / 12)

while month < 12:
    month += 1
    minPayment = round(monthlyPaymentRate * balance, 2)
    totalPaid = round(totalPaid + minPayment, 2)
    newBalance = (balance - minPayment)
    balance = newBalance + round(monthlyInterestRate * newBalance, 2)
    print ('Month: ' + str(month))
    print ('Minimum monthly payment: ' + str(minPayment))
    print ('Remaining balance: ' + str(balance))
    
print ('Total paid: ' + str(totalPaid))
print ('Remaining balance: ' + str(balance))
