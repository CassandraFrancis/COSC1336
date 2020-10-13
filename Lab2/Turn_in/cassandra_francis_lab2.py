# Miles to kilometers – one mile = 1.6 kilometers  (miles * 1.6)
miles = float(input('Hi, please enter the number of miles you would like to convert to kilometers: '))
miles_km = miles * 1.6
print(miles, 'miles is equal to', format(miles_km, '.2f'), 'kilometers')

# Fahrenheit to Celsius – the formula to calculate is (F - 32) * 5/9 where F is the Fahrenheit temperature
F = float(input('Alright, now enter the fahrenheit temperature you would like to convert to celsius: '))
F_C = (F - 32) * 5/9
print(format(F_C, '.1f'), 'degrees celsius is the same temperature as', F, 'degrees fahrenheit ')

# Gallons to liters – one gallon = 3.9 liters (gallons * 3.9)
gal = float(input('Ok, now enter the number of gallons you would like converted to liters: '))
gal_lit = gal * 3.9
print(format(gal_lit, '.2f'), 'liters is equivalent to', gal, 'gallons.')

# Pounds to kilograms – one pound = 0.45 kilograms (pounds * 0.45)
lbs = float(input('How many pounds would you like converted to kilograms? ' ))
lbs_kilo = lbs * 0.45
print(format(lbs_kilo, '.2f'), 'kilograms is the same weight as', lbs, 'pounds!')

# Inches to centimeters – one inch = 2.54 centimeters (inch * 2.54)
inch = float(input('Enter the number of inches you need converted to centimeters: ' ))
inch_cm = inch * 2.54
print('There are', format(inch_cm, '.2f'), 'centimeters in', inch, 'inches')
