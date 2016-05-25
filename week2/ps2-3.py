
def unpaidBalance(balance, payment):
  return balance - payment

def updatedBalance(balance, payment):
  return unpaidBalance(balance, payment) * (1 + annualInterestRate / 12.0)

def tryToPay(balance, payment):
  for i in range(12):
    balance = updatedBalance(balance, payment)

  return balance

balance = 8
annualInterestRate = 0.25

lo = balance / 12.0
hi = (balance * (1 + annualInterestRate / 12.0) ** 12) / 12.0

payment = (lo + hi) / 2
finalBalance = tryToPay(balance, payment)

while abs(finalBalance) > 0.01:
  if finalBalance > 0:
    lo = payment
  else:
    hi = payment

  payment = (lo + hi) / 2
  finalBalance = tryToPay(balance, payment)

print 'Lowest Payment: ' + str(round(payment,2))
