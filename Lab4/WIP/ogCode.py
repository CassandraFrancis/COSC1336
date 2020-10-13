# error handling for negative numbers
def not_neg(entry):
    counter = 0
    while counter < 2:
        if entry < 0:
            counter += 1
            print('Invalid input. You must enter a positive number.')
            entry = float(input('Enter a correct value: '))
        else:
            return entry
    return entry


# error handling for temp over 1000
def too_hot(entry):
    counter = 0
    while counter < 2:
        if entry > 1000:
            counter += 1
            print('Invalid input. You must enter a temperature below 1000.')
            entry = float(input('Enter a correct value: '))
        else:
            return entry
    return entry


miles = not_neg(float(input('Please enter the number of miles you would like to convert to kilometers: ')))  # get number of miles
if miles >= 0:  # miles-km valid input
    miles_km = miles * 1.6  # calculate miles-km
    print(miles, 'miles is equal to', format(miles_km, '.2f'), 'kilometers')  # display mi-km conversion
    F = too_hot(float(input('What is the fahrenheit temperature would you like converted to celsius?: ')))  # get temp
    if F <= 1000:  # Fah-cel valid input
        F_C = (F - 32) * 5 / 9  # calculate fahr-cels
        print(format(F_C, '.1f'), 'degrees celsius is the same temperature as', F, 'degrees fahrenheit ')  # display F-C conversion
        gal = not_neg(float(input('Enter the number of gallons you would like converted to liters: ')))  # get number of gallons
        if gal >= 0:  # gal-lit valid input
            gal_lit = gal * 3.9  # calculate gal-lit
            print(format(gal_lit, '.2f'), 'liters is equivalent to', gal, 'gallons.')  # display gal-lit conversion
            lbs = not_neg(float(input('How many pounds would you like converted to kilograms?: ')))  # get number of pounds/lbs
            if lbs >= 0:  # lbs-kg valid input
                lbs_kilo = lbs * 0.45  # calculate lsb-kg
                print(format(lbs_kilo, '.2f'), 'kilograms is the same weight as', lbs, 'pounds!')  # display lbs-kg conversion
                inch = not_neg(float(input('Enter the number of inches you need converted to centimeters: ')))  # get number of inches
                if inch >= 0:  # in-cm valid input
                    inch_cm = inch * 2.54  # calculate in-cm
                    print('There are', format(inch_cm, '.2f'), 'centimeters in', inch, 'inches')  # display in-cm conversion
                else:
                    print('**ERROR** \nInvalid input, cannot calculate negative inches')  # if inches entered is negative
            else:
                print('**ERROR** \n Invalid input, cannot calculate negative pounds')  # if pounds entered is negative
        else:
            print('**ERROR** \n Invalid input, cannot calculate negative gallons')  # if gallons entered is negative
    else:
        print('**ERROR** \n Invalid input, cannot calculate fahrenheit temperature over 1000 degrees')  # if temp entered is over 1000
else:
    print('**ERROR** \n Invalid input, cannot calculate negative miles')  # if miles entered is negative
