# # #
# # # counter = 0
# # # miles = float(input('Please enter the number of miles you would like to convert to kilometers: '))
# # # while miles < 0 and counter <= 2:
# # #     print('Invalid input. You must enter a positive number.')
# # #     miles = float(input('Enter the number of miles you would like converted to kilometers: '))
# # #     counter = counter + 1
# # # if counter <= 2 or miles >= 0:
# # #     miles_km = miles * 1.6  # calculate miles-km
# # #     print(miles, 'miles is equal to', format(miles_km, '.2f'), 'kilometers')
# # # F = float(input('What is the fahrenheit temperature would you like converted to celsius?: '))  # get temp
# # # if F <= 1000:  # Fah-cel valid input
# # #     F_C = (F - 32) * 5/9  # calculate fahr-cels
# # #     print(format(F_C, '.1f'), 'degrees celsius is the same temperature as', F, 'degrees fahrenheit ')
# # # else:
# # #     print('**ERROR** \n Invalid input, cannot calculate negative miles')  # strike 3!
# #
# #
# # # This program averages test scores. It asks the user for the
# # # number of students and the number of test scores per student.
# #
# # # Get the number of students.
# # num_students = int(input('How many students do you have? '))
# #
# # # Get the number of test scores per student.
# # num_test_scores = int(input('How many test scores per student? '))
# #
# # # Determine each students average test score.
# # for student in range(num_students):
# #     # Initialize an accumulator for test scores.
# #     total = 0.0
# #     # Get a student's test scores.
# #     print('Student number', student + 1)
# #     print('-----------------')
# #     for test_num in range(num_test_scores):
# #         print('Test number', test_num + 1, end='')
# #         score = float(input(': '))
# #         # Add the score to the accumulator.
# #         total += score
# #
# #     # Calculate the average test score for this student.
# #     average = total / num_test_scores
# #
# #     # Display the average.
# #     print('The average for student number', student + 1, \
# #           'is:', format(average, '.1f'))
# #     print()
# #
#
#
#
# valid_entry_neg = 'yes'
# valid_entry_temp = 'yes'
# counter = 0
# # miles to kilometers
# miles = (float(input('Please enter the number of miles you would like to convert to kilometers: ')))  # get number of miles
# if miles >= 0 and valid_entry_neg == 'yes':  # if correct on first try
#     miles_km = miles * 1.6  # calculate miles-km
#     print(format(miles_km, '.2f'), ' kilometers is equal to ', miles, ' miles.')  # display mi-km conversion
#
# while miles < 0 and valid_entry_neg == 'yes':  # loop for incorrect input (4 tries)
#     counter += 1
#     print('Invalid input. You must enter a positive number.')  # instruction statement
#     miles = float(input('Enter a positive mileage: '))  # re-enter miles
#
#     if miles >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
#         valid_entry = 'yes'
#         miles_km = miles * 1.6  # calculate miles-km
#         print(format(miles_km, '.2f'), ' kilometers is equal to ', miles, ' miles.')  # display mi-km conversion
#
#     if miles < 0 and counter == 3:
#         print('**ERROR** \n Invalid input, cannot calculate negative miles')  # if miles entered is negative 4th time
#         valid_entry_neg = 'no'
#
# # Fahrenheit to Celsius
# if valid_entry_temp == 'yes':
#     counter = 0
#     fahr = (float(input('What is the fahrenheit temperature would you like converted to celsius?: ')))  # get temp
#
#     if fahr <= 1000:  # if correct on first try
#         valid_entry_temp = 'yes'
#         fahr_cels = (fahr - 32) * 5 / 9  # calculate fahr-cels
#         print(format(fahr_cels, '.1f'), 'degrees celsius is the same temperature as', fahr, 'degrees fahrenheit ')  # display fahr_cels conversion
#
#     while fahr > 1000 and valid_entry_temp == 'yes':
#         counter += 1
#         print('Invalid input. You must enter a temperature under 1000 degrees fahrenheit.')
#         fahr = float(input('Enter a lower temperature: '))
#
#         if fahr <= 1000 and counter <= 3:
#             valid_entry_temp = 'yes'
#             fahr_cels = (fahr - 32) * 5 / 9  # calculate fahr-cels
#             print(format(fahr_cels, '.1f'), 'degrees celsius is the same temperature as', fahr, 'degrees fahrenheit ')  # display F-C conversion
#
#         if fahr > 1000 and counter == 3:
#             print('**ERROR** \n Invalid input, cannot calculate fahrenheit temperature over 1000 degrees')
#             valid_entry_temp = 'no'
#
# # Gallons to liters
# if valid_entry_neg == 'yes':
#     counter = 0
#     gal = (float(input('Enter the number of gallons you would like converted to liters: ')))  # get number of gallons
#
#     if gal >= 0:  # if correct on first try
#         valid_entry_neg = 'yes'
#         gal_lit = gal * 3.9  # calculate gal-lit
#         print(format(gal_lit, '.2f'), 'liters is equivalent to', gal, 'gallons.')  # display gal-lit conversion
#
#     while gal < 0 and valid_entry_neg == 'yes':  # loop for incorrect input (4 tries)
#         counter += 1
#         print('Invalid input. You must enter a positive number.')  # instruction statement
#         gal = float(input('Enter a positive number of gallons: '))  # re-enter gals
#
#         if gal >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
#             valid_entry_neg = 'yes'
#             gal_lit = gal * 3.9  # calculate gal-lit
#             print(format(gal_lit, '.2f'), 'liters is equivalent to', gal, 'gallons.')  # display gal-lit conversion
#
#         if gal < 0 and counter == 3:
#             print('**ERROR** \n Invalid input, cannot calculate negative gallons')  # if gals entered is negative 4th time
#             valid_entry = 'no'
#
# # pounds to kilograms
# if valid_entry_neg == 'yes':
#     counter = 0
#     lbs = (float(input('How many pounds would you like converted to kilograms?: ')))  # get number of pounds/lbs
#
#     if lbs >= 0:  # if correct on first try
#         valid_entry_neg = 'yes'
#         lbs_kg = lbs * 0.45  # calculate lsb-kg
#         print(format(lbs_kg, '.2f'), 'kilograms is the same weight as', lbs, 'pounds!')  # display lbs-kg conversion
#
#     while lbs < 0 and valid_entry_neg == 'yes':  # loop for incorrect input (4 tries)
#         counter += 1
#         print('Invalid input. You must enter a positive number.')  # instruction statement
#         lbs = float(input('Enter a positive weight: '))  # re-enter gals
#
#         if lbs >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
#             valid_entry_neg = 'yes'
#             lbs_kg = lbs * 0.45  # calculate lsb-kg
#             print(format(lbs_kg, '.2f'), 'kilograms is the same weight as', lbs, 'pounds!')  # display lbs-kg conversion
#
#         if lbs < 0 and counter == 3:
#             print('**ERROR** \n Invalid input, cannot calculate negative gallons')  # if lbs entered is negative 4th time
#             valid_entry_neg = 'no'
#
# # inches to centimeters
# if valid_entry_neg == 'yes':
#     counter = 0
#     inch = (float(input('Enter the number of inches you need converted to centimeters: ')))  # get number of inches
#
#     if inch >= 0:  # if correct on first try
#         valid_entry_neg = 'yes'
#         inch_cm = inch * 2.54  # calculate in-cm
#         print('There are', format(inch_cm, '.2f'), 'centimeters in', inch, 'inches')  # display in-cm conversion
#
#     while inch < 0 and valid_entry_neg == 'yes':  # loop for incorrect input (4 tries)
#         counter += 1
#         print('Invalid input. You must enter a positive number.')  # instruction statement
#         lbs = float(input('Enter a positive length: '))  # re-enter gals
#
#         if inch >= 0 and counter <= 3:  # if wrong entries less than 4 and correct value entered
#             valid_entry_neg = 'yes'
#             inch_cm = inch * 2.54  # calculate in-cm
#             print('There are', format(inch_cm, '.2f'), 'centimeters in', inch, 'inches')  # display in-cm conversion
#
#         if inch < 0 and counter == 3:
#             valid_entry_neg = 'no'
#             print('**ERROR** \nInvalid input, cannot calculate negative inches')  # if lbs entered is negative 4th time
#
# if valid_entry_neg == 'no':
#     print('**ERROR** \nInvalid input, cannot calculate a negative value')
# elif valid_entry_temp == 'no':
#     print('**ERROR** \n Invalid input, cannot calculate fahrenheit temperature over 1000 degrees')
# else:
#     print('I hope this conversion program helped you!')
#
#
# Lab4a Cassandra Francis user cannot enter a negative number for; miles, gal, lbs or inch user cannot enter a temp
# above 1000 F # If the user enters an invalid value more than three times in a row, the program should issue an
# error message and stop

global valid_entries


def main():
    global valid_entries
    valid_entries = 1

    get_entry('miles', 'kilometers')
    if valid_entries == 1:
        get_entry('gallons', 'liters')
    if valid_entries == 1:
        get_entry('pounds', 'kilograms')
    if valid_entries == 1:
        get_entry('inches', 'centimeters')
    if valid_entries == 1:
        get_entry('fahrenheit', 'celsius ')
    return


# error handling for negative numbers
def not_neg(entry, us, metric):
    counter = 0
    while counter < 2:
        if entry < 0:
            counter += 1
            print('Invalid input. You must enter a positive number.')
            entry = float(input('Enter a correct value: '))
        else:
            counter=2

    if :
        global valid_entries
        valid_entries = 0
        print('**ERROR** \n Invalid input, cannot calculate negative ', us)
        return

        result = convert(us, entry,)
    display_result(us, metric, result, entry)
    return






# error handling for temp over 1000
def too_hot(entry, us, metric):
    counter = 0
    while counter <= 2:
        if entry > 1000:
            counter += 1
            print('Invalid input. You must enter a temperature below 1000.')
            entry = float(input('Enter a correct value: '))
        else:
            result = convert(us, entry)
            display_result(us, metric, result, entry)
    if counter >= 2:
        global valid_entries
        valid_entries = 0
        print('**ERROR** \n Invalid input, cannot calculate fahrenheit temperature over 1000 degrees')


def convert(us, entry):
    if us == 'miles':
        return entry * 1.6  # calculate miles-km
    elif us == 'gallons':
        return entry * 3.9  # calculate gal-lit
    elif us == 'pounds':
        return entry * 0.45  # calculate las-kg
    elif us == 'inches':
        return entry * 2.54  # calculate in-cm
    else:
        return (entry - 32) * 5 / 9  # calculate fahr-cels


def display_result(us, metric, result, entry):
    print(entry, us, ' is equal to ', format(result, '.2f'), metric)


def get_entry(us, metric):
    entry = float(input('Please enter the ' + us + ' you want converted into ' + metric + ': '))
    if us == 'fahrenheit':
        entry = too_hot(entry, us, metric)
    else:
        entry = not_neg(entry, us, metric)


main()
