
# starting thresholds
valid_entry = 'yes'
counter = 0
print('This program will help you convert US measurements to Metric measurements. \n'
      'Please enter only positive values for Miles, Gallons, Pounds, and Inches '
      'and less than 1000 for Fahrenheit temperature.\nJust follow the on screen prompts.')
# Distance - miles to kilometers
miles = (float(input('Please enter the number of miles you would like to convert to kilometers: ')))  # get number of miles
while (miles < 0 and valid_entry == 'yes') or (counter == 0):  # checks first entry, valid goes to 1st "if" invalid goes to 2nd "if"

    if miles < 0 and counter == 3:  # checking for 4th incorrect entry (counter at 3)
        valid_entry = 'no'  # tells program not to move on to next question after 4 invalid entries
        print('**ERROR** \nInvalid input, cannot calculate negative miles')  # error message

    elif miles < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (counter 1-2)
        counter += 1  # adds 1 to counter for each incorrect value
        print('Invalid input. You must enter a positive number.')  # instruction statement for incorrect value
        miles = float(input('Enter a positive mileage: '))  # asking for correct input

    if miles >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
        valid_entry = 'yes'  # tells program to move on to the next question
        miles_km = miles * 1.6  # calculate miles-km
        print(format(miles_km, '.2f'), ' kilometers is equal to ', miles, ' miles.')  # display mi-km conversion
        counter = -1  # exit statement

# Temperature - fahrenheit to celsius
if valid_entry == 'yes':  # executes if previous ends as a valid entry
    counter = 0  # reset counter
    fahr = (float(input('What is the fahrenheit temperature would you like converted to celsius?: ')))  # get temp
    while (fahr > 1000 and valid_entry == 'yes') or (counter == 0): # checks first entry invalid goes to 1st "if" valid goes to 2nd "if"

        if fahr > 1000 and counter == 3:  # checking for 4th incorrect entry (counter at 3)
            valid_entry = 'no'  # tells program not to move on to next question after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate fahrenheit temperature over 1000 degrees')  # error message
        elif fahr > 1000 and counter < 3:  # checking for invalid entry for tries 1-3 (counter 1-2)
            counter += 1  # adds 1 to counter for each incorrect value
            print('Invalid input. You must enter a temperature under 1000 degrees fahrenheit.')  # instruction statement for incorrect value
            fahr = float(input('Enter a lower temperature: '))  # asking for correct input

        if fahr <= 1000 and counter <= 3:  # if wrong entries less than 4 and correct value entered
            valid_entry = 'yes'  # tells program to move on to the next question
            fahr_cels = (fahr - 32) * 5 / 9  # calculate fahr-cels
            print(format(fahr_cels, '.1f'), 'degrees celsius is the same temperature as', fahr, 'degrees fahrenheit ')  # display F-C conversion
            counter = -1 # exit statement

# Volume - Gallons to Liters
if valid_entry == 'yes':  # executes if previous ends as a valid entry
    counter = 0  # reset counter
    gal = (float(input('Enter the number of gallons you would like converted to liters: ')))  # get number of gallons

    while (gal < 0 and valid_entry == 'yes') or (counter == 0):  # checks first entry, valid goes to 1st "if" invalid goes to 2nd "if"

        if gal < 0 and counter == 3:  # checking for 4th incorrect entry (counter at 3)
            valid_entry = 'no'  # tells program not to move on to next question after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate negative gallons')  # error message

        elif gal < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (counter 1-2)
            counter += 1  # adds 1 to counter for each incorrect value
            print('Invalid input. You must enter a positive number.')  # instruction statement for incorrect value
            gal = float(input('Enter a positive number of gallons: '))  # asking for correct input

        if gal >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
            valid_entry = 'yes'  # tells program to move on to the next question
            gal_lit = gal * 3.9  # calculate gal-lit
            print(format(gal_lit, '.2f'), 'liters is equivalent to', gal, 'gallons.')  # display gal-lit conversion
            counter = -1  # exit statement

# Weight - pounds to kilograms
if valid_entry == 'yes':  # executes if previous ends as a valid entry
    counter = 0
    lbs = (float(input('How many pounds would you like converted to kilograms?: ')))  # get number of pounds/lbs

    while (lbs < 0 and valid_entry == 'yes') or (counter == 0):  # checks first entry, valid goes to 1st "if" invalid goes to 2nd "if"

        if lbs < 0 and counter == 3:  # checking for 4th incorrect entry (counter at 3)
            valid_entry = 'no'  # tells program not to move on to next question after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate negative pounds')  # error message

        elif lbs < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (counter 1-2)
            counter += 1  # adds 1 to counter for each incorrect value
            print('Invalid input. You must enter a positive number.')  # instruction statement for incorrect value
            lbs = float(input('Enter a positive amount: '))  # asking for correct input

        if lbs >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
            valid_entry = 'yes'  # tells program to move on to the next question
            lbs_kg = lbs * 0.45  # calculate lsb-kg
            print(format(lbs_kg, '.2f'), 'kilograms is the same weight as', lbs, 'pounds!')  # display lbs-kg conversion
            counter = -1  # exit statement


# Length - inches to centimeters
if valid_entry == 'yes':
    counter = 0
    inch = (float(input('Enter the number of inches you need converted to centimeters: ')))  # get number of inches

    while (inch < 0 and valid_entry == 'yes') or (counter == 0):  # checks first entry, valid goes to 1st "if" invalid goes to 2nd "if"

        if inch < 0 and counter == 3:  # checking for 4th incorrect entry (counter at 3)
            valid_entry = 'no'  # tells program not to move on to next question after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate negative inches')  # error message

        elif inch < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (counter 1-2)
            counter += 1  # adds 1 to counter for each incorrect value
            print('Invalid input. You must enter a positive number.')  # instruction statement for incorrect value
            inch = float(input('Enter a positive number of inches: '))  # asking for correct input

        if inch >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
            valid_entry = 'yes'  # tells program to move on to the next question
            inch_cm = inch * 2.54  # calculate in-cm
            print('There are', format(inch_cm, '.2f'), 'centimeters in', inch, 'inches')  # display in-cm conversion
            counter = -1  # exit statement
if valid_entry == 'yes':
    print()
    print('I hope you found this US to Metric conversion program helpful!')
else:
    print()
    print('Please pay attention to the instructions! \nYou will need to re-start the program to try again.')
