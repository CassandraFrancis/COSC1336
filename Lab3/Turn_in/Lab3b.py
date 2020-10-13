# Lab 3b Cassandra Francis

# starting values
base_pay = 2000.00
deduction = 0
sales_bonus = 0
adtl_bonus = 0
gross_pay = 0

# input from user
print('Hello! I\'m going to help you calculate your sales team\'s pay. I\'ll need to get some information from you first.')
name = input('Please enter the salesperson\'s name: ')
mths_employed = float(input('Please enter the total number of months they have been employed: '))
vacay = float(input('Please enter the number of vacations days they have taken this month: '))
sales = float(input('Please enter their total sales for the month: '))

if sales > 1000000:  # sales over $1 mil
    commission_rate = 0.35
    sales_bonus = 100000
elif 500001 <= sales <= 1000000:  # sales between $500,001-1 mil
    commission_rate = 0.28
    sales_bonus = 5000
elif 100001 <= sales <= 500000:  # sales between $100,001-500k
    commission_rate = 0.15
    sales_bonus = 1000
elif 10000 <= sales <= 100000:  # sales between 10k-100k
    commission_rate = 0.02
    sales_bonus = 0
else:  # sales less than 10k
    commission_rate = 0
    sales_bonus = 0

if mths_employed < 3:  # no sales bonus for employment less than 3 months
    sales_bonus = 0

if mths_employed >= 60 and sales > 100000:  # additional bonus for 5+ years & more than $100k sales
    adtl_bonus = 1000

if vacay > 3:  # $200 pay deduction for more then 3 vacation days
    deduction = 200

# calculations
commission = (sales * commission_rate)  # calculate commission rate
gross_pay = base_pay + commission + sales_bonus + adtl_bonus - deduction  # calculate gross pay
print('--------------------------------------------')
print('Employee Name: ', name)
print('Length of employment: ', format(mths_employed, '.2f'), 'months')
print('=====PAY STUB=====')
print(' ${:,.2f}'.format(base_pay), '   Base Monthly Salary',  sep='')
print(' ${:,.2f}'.format(commission), '   Commissions Earned', sep='')
print(' ${:,.2f}'.format(sales_bonus), '   Sales Bonus Earned', sep='')
print(' ${:,.2f}'.format(adtl_bonus), '   Additional Bonuses Earned', sep='')
print('-${:,.2f}'.format(deduction), '   Pay Deductions', sep='')
print()
print(' ${:,.2f}'.format(gross_pay), '   Gross Monthly Pay', sep='')
