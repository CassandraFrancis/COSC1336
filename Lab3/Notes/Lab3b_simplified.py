# monthly base pay
base_pay = 2000.00

# get input from user
name = input('Please enter the salespersons name: ')
sales = float(input('Please enter their total sales for the month: '))
mths_employed = float(input('Please enter the total number of months they have been employed: '))
vacay = float(input('Please enter the number of vacations days they have taken this month: '))

# sales thresholds
sales_bracket1 = 10000
sales_bracket2 = 100000
sales_bracket3 = 500000
sales_bracket4 = 1000000
# calculate base pay, commissions and sales bonus for each sales bracket
if sales <= sales_bracket2:
    commission_rate = sales * 0.02
    sales_bonus = 0
elif sales <= sales_bracket3:
    commission_rate = sales * .15
    if mths_employed >= 3:
        sales_bonus = 1000
    else:
        sales_bonus = 0
elif sales <= sales_bracket4:
    commission_rate = sales * .28
    if mths_employed >= 3:
        sales_bonus = 5000
    else:
        sales_bonus = 0
elif sales > sales_bracket4:
    commission_rate = sales * .35
    if mths_employed >= 3:
        sales_bonus = 100000
    else:
        sales_bonus = 0
else:
    commission_rate = sales * 0
    sales_bonus = 0

# standard pay before deductions and 5 year bonus
earnings = base_pay + commission_rate + sales_bonus

# calculate pay with or without 5 year bonus
if mths_employed >= 60 and sales > sales_bracket2:
    adtl_bonus = 1000
    total_pay = earnings + adtl_bonus
else:
    adtl_bonus = 0
    total_pay = earnings

# Calculate pay with or without vacation deduction
if vacay > 3:
    deduction = 200
    total_pay = earnings - deduction
else:
    deduction = 0
    total_pay = earnings

# Display pay stub
print('Employee Name: ', name)
print('Length of employment: ', format(mths_employed, '.2f'), 'months')
print('Base Monthly Salary: $', format(base_pay, ',.2f'), sep='')
print('Commissions Earned: $', format(commission_rate, ',.2f'), sep='')
print('Sales Bonus Earned: $', format(sales_bonus, ',.2f'), sep='')
print('Additional Bonuses Earned: $', format(adtl_bonus, ',.2f'), sep='')
print('Pay Deductions: $', format(deduction, ',.2f'), sep='')
print('Gross Monthly Pay: $', format(total_pay, ',.2f'), sep='')
