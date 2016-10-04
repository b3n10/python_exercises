#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
This program calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
A fixed monthly payment is a single number which does not change each month, but instead is a constant amount that will be paid each month.
'''

def main(balance, fixedMonthlyPayment, annualInterestRate, month):
    '''
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    '''
    if month == 12:
        return balance
    else:
        '''
        Monthly interest rate = (Annual interest rate) / 12.0
        Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
        Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        '''
        balance = balance - fixedMonthlyPayment
        monthlyInterestRate = annualInterestRate / 12.0
        balance = balance + (monthlyInterestRate * balance)
        return main(balance, fixedMonthlyPayment, annualInterestRate, month + 1)

balance = 3926
annualInterestRate = 0.2
month = 0

def loop():
    fixedPayment = 0

    while ( main(balance, fixedPayment, annualInterestRate, month) >= 0 ):
        fixedPayment = fixedPayment + 10
    
    return fixedPayment

print("balance: " + str(balance) + "\n" + "annual interest rate: " + str(annualInterestRate))
print("Lowest payment: " + str(loop()))


