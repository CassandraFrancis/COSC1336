# Cassandra Francis Lab 4a
# For this portion of the lab, you will reuse the program you wrote in Lab 3A.  Redesign this solution so that some portions of the code are repeated.  
# Now you will add a loop such that the user gets three changes to enter a valid value.  
# If the user enters an invalid value more than three times in a row, the program should issue an error message and terminate. 

# starting thresholds and explaination/instructions
validEntry = 'yes'
counter = 0
print('This program will help you convert US measurements to Metric measurements. \n'
      '\nPlease enter only positive values for Miles, Gallons, Pounds, and Inches '
      'and less than 1000 for Fahrenheit temperature.\n\nJust follow the on screen prompts below.')
# Distance - miles to kilometers
miles = (float(input('\nPlease enter the number of miles you would like to convert to kilometers: ')))  # user input; number of miles
while (miles < 0 and validEntry == 'yes') or (counter == 0):  # checks first entry, valid goes to 2nd "if" invalid goes to 1st "if"

    if miles < 0 and counter == 3:  # checking for 4th incorrect entry (aka counter at 3)
        validEntry = 'no'  # tells program not to move on after 4 invalid entries
        print('**ERROR** \nInvalid input, cannot calculate negative miles')  # error message after 4 failed attempts 

    elif miles < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (aka counter 1-2)
        counter += 1  # adds 1 to counter for each invalid value
        print('Invalid input. You must enter a positive number.')  # instruction statement for invalid value
        miles = float(input('Enter a positive mileage: '))  # user input; asking for valid value

    if miles >= 0 and counter <= 3:  # if invalid entries less than 4 and correct value entered
        validEntry = 'yes'  # tells program to move forward
        miToKm = miles * 1.6  # calculate miles-km
        print(format(miToKm, ',.2f'), ' kilometers is equal to ', format(miles, ',.2f'), ' miles.')  # display mi-km conversion
        counter = -1  # exit statement

# Temperature - fahrenheit to celsius
if validEntry == 'yes':  # executes if previous measurement ends as a valid entry
    counter = 0  # reset counter
    fah = (float(input('\nWhat is the fahrenheit temperature would you like converted to celsius?: ')))  # user input; temp
    while (fah > 1000 and validEntry == 'yes') or (counter == 0): # checks first entry, invalid goes to 1st "if" valid goes to 2nd "if"

        if fah > 1000 and counter == 3:  # checking for 4th incorrect entry (aka counter at 3)
            validEntry = 'no'  # tells program not to move on after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate fahrenheit temperature over 1000 degrees')  # error message after 4 failed attempts
        elif fah > 1000 and counter < 3:  # checking for invalid entry for tries 1-3 (aka counter 1-2)
            counter += 1  # adds 1 to counter for each incorrect value
            print('Invalid input. You must enter a temperature under 1000 degrees fahrenheit.')  # instruction statement for invalid value
            fah = float(input('Enter a lower temperature: '))  # user input; asking for valid input

        if fah <= 1000 and counter <= 3:  # if invalid entries less than 4 and valid value entered
            validEntry = 'yes'  # tells program to move forward
            fahToCel = (fah - 32) * 5 / 9  # calculate fahr-cels
            print(format(fahToCel, '.2f'), 'degrees celsius is the same temperature as', format(fah, '.2f'), 'degrees fahrenheit ')  # display F-C conversion
            counter = -1 # exit statement

# Volume - Gallons to Liters
if validEntry == 'yes':  # executes if previous measurement ends as a valid entry
    counter = 0  # reset counter
    gal = (float(input('\nEnter the number of gallons you would like converted to liters: ')))  # user input; number of gallons

    while (gal < 0 and validEntry == 'yes') or (counter == 0):  # checks first entry, valid goes to 2nd "if" invalid goes to 1st "if"

        if gal < 0 and counter == 3:  # checking for 4th invalid entry (aka counter at 3)
            validEntry = 'no'  # tells program not to move on after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate negative gallons')  # error message ater 4 failed attempts

        elif gal < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (aka counter 1-2)
            counter += 1  # adds 1 to counter for each invalid value
            print('Invalid input. You must enter a positive number.')  # instruction statement for invalid value
            gal = float(input('Enter a positive number of gallons: '))  # user input; asking for valid value

        if gal >= 0 and counter <= 3:  # if invalid entries less than 4 and valid value entered
            validEntry = 'yes'  # tells program to move forward
            galToLit = gal * 3.9  # calculate gal-lit
            print(format(galToLit, ',.2f'), 'liters is equivalent to', format(gal, ',.2f'), 'gallons.')  # display gal-lit conversion
            counter = -1  # exit statement

# Weight - pounds to kilograms
if validEntry == 'yes':  # executes if previous ends as a valid entry
    counter = 0  # reset counter
    lbs = (float(input('\nHow many pounds would you like converted to kilograms?: ')))  # user input; number of pounds/lbs

    while (lbs < 0 and validEntry == 'yes') or (counter == 0):  # checks first entry, valid goes to 2nd "if" invalid goes to 1st "if"

        if lbs < 0 and counter == 3:  # checking for 4th invalid  entry (aka counter at 3)
            validEntry = 'no'  # tells program not to move on after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate negative pounds')  # error message after 4 failed attempts

        elif lbs < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (aka counter 1-2)
            counter += 1  # adds 1 to counter for each invalid value
            print('Invalid input. You must enter a positive number.')  # instruction statement for invalid value
            lbs = float(input('Enter a positive amount: '))  # user inout; asking for valid value

        if lbs >= 0 and counter <= 3:  # if invalid entries less than 4 and correct value entered
            validEntry = 'yes'  # tells program to move forward
            lbsToKg = lbs * 0.45  # calculate lsb-kg
            print(format(lbsToKg, ',.2f'), 'kilograms is the same weight as', format(lbs, ',.2f'), 'pounds!')  # display lbs-kg conversion
            counter = -1  # exit statement


# Length - inches to centimeters
if validEntry == 'yes':  # executes if previous measurement ends as a valid entry
    counter = 0  #reset counter
    inch = (float(input('\nEnter the number of inches you need converted to centimeters: ')))  # user input; number of inches

    while (inch < 0 and validEntry == 'yes') or (counter == 0):  # checks first entry, valid goes to 2nd "if" invalid goes to 1st "if"

        if inch < 0 and counter == 3:  # checking for 4th incorrect entry (aka counter at 3)
            validEntry = 'no'  # tells program not to move on after 4 invalid entries
            print('**ERROR** \nInvalid input, cannot calculate negative inches')  # error message for 4 failed attempts

        elif inch < 0 and counter < 3:  # checking for invalid entry for tries 1-3 (aka counter 1-2))
            counter += 1  # adds 1 to counter for each invalid value
            print('Invalid input. You must enter a positive number.')  # instruction statement for invalid value
            inch = float(input('Enter a positive number of inches: '))  # user input; asking for valid value

        if inch >= 0 and counter <= 3:  # if invalid entries less than 4 and correct value entered
            validEntry = 'yes'  # tells program to move forward
            inToCm = inch * 2.54  # calculate in-cm
            print('There are', format(inToCm, ',.2f'), 'centimeters in', format(inch, ',.2f'), 'inches')  # display in-cm conversion
            counter = -1  # exit statement

if validEntry == 'yes':  # display the following if user gets through whole program
    print()  # blank line
    print('I hope you found this US to Metric conversion program helpful!')  # # displayed if user gets through whole program
else:  # display the following after the error message from 4 failed attempts
    print()  # blank line
    print('Please pay attention to the instructions! \nYou will need to re-start the program to try again.')  # displayed after the error message from 4 failed attempts
