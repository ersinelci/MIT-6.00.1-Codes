#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#The following variables contain values as described below:

#balance - the outstanding balance on the credit card

#annualInterestRate - annual interest rate as a decimal

#monthlyPaymentRate - minimum monthly payment rate as a decimal

#For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance.

def balancecalculator(balance,annualInterestRate,monthlyPaymentRate):
   
    
    counter = 0
    while(counter < 12  ):
        
        balance = balance + balance*(annualInterestRate/12)
        balance = balance - balance*monthlyPaymentRate
        balance =  round(balance,2)
        
        counter = counter + 1
    print(balance)        
    return balance

    
balancecalculator(42, 0.2, 0.04)
