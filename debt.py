#!/usr/bin/python3

def main(balance, annualInterestRate, monthlyPaymentRate, month):
    '''
    Monthly interest rate= (Annual interest rate) / 12.0 * balance
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    '''
    print("Month: " + str(month) + ", balance: " + str(round(balance, 2)))
    if month == 12:
        return round(balance, 2)
    else:
        monthlyInterestRate = annualInterestRate / 12
        min_monthlyPayment = monthlyPaymentRate * balance
        balance = balance -  min_monthlyPayment
        balance = balance + (monthlyInterestRate * balance)
        return main(balance, annualInterestRate, monthlyPaymentRate, month + 1)

if __name__ == "__main__":
    print( main(5000, 0.18, 0.02, 0) )
