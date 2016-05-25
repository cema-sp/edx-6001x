
def unpaidBalance(balance, payment):
  return balance - payment

def updatedBalance(balance, payment):
  return unpaidBalance(balance, payment) * (1 + annualInterestRate / 12.0)

balance = 4842
annualInterestRate = 0.2

def tryToPay(balance, payment):
  for i in range(12):
    balance = updatedBalance(balance, payment)

  return balance

balance = 8
annualInterestRate = 0.25

for payment in range(10, max(balance, 10) + 1, 10):
  if tryToPay(balance, payment) <= 0:
    break

print 'Lowest Payment: ' + str(payment)
