def minPayment(balance):
  return monthlyPaymentRate * balance

def unpaidBalance(balance):
  return balance - minPayment(balance)

def updatedBalance(balance):
  return unpaidBalance(balance) * (1 + annualInterestRate / 12.0)

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0

for i in range(12):
  print 'Month: ' + str(i + 1)
  minPay = minPayment(balance)
  totalPaid += minPay
  print 'Minimum monthly payment: ' + str(round(minPay,2))
  balance = updatedBalance(balance)
  print 'Remaining balance: ' + str(round(balance,2))

print 'Total paid: ' + str(round(totalPaid, 2))
print 'Remaining balance: ' + str(round(balance,2))
