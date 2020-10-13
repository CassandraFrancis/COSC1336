# Lab4a Cassandra Francis
# user cannot enter a negative number for; miles, gal, lbs or inch
# user cannot enter a temp above 1000 F
# # If the user enters an invalid value more than three times in a row, the program should issue an error message and stop

# error handling for negative numbers
def not_neg(entry, us, metric):
    counter = 0
    while counter < 2:
        if entry < 0:
            counter += 1
            print('Invalid input. You must enter a positive number.')
            entry = float(input('Enter a correct value: '))
        else:
            result = convert(us, entry)
            display_result(us, metric, result, entry)
    if counter > 1:
        valid_entries = 0
        print('ERROR')

# error handling for temp over 1000
def too_hot(entry, us, metric):
    counter = 0
    while counter < 2:
        if entry > 1000:
            counter += 1
            print('Invalid input. You must enter a temperature below 1000.')
            entry = float(input('Enter a correct value: '))
        else:
            result = convert(us, entry)
            display_result(us, metric, result, entry)


def convert(us, entry):
    if us == 'miles':
        return entry * 1.6  # calculate miles-km
    elif us == 'gallons':
        return entry * 3.9  # calculate gal-lit
    elif us == 'pounds':
        return entry * 0.45  # calculate las-kg
    elif us == 'inches':
        return entry * 2.54 # calculate in-cm
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

valid_entries = 1

while valid_entries != 0:
    get_entry('miles', 'kilometers')
    get_entry('gallons', 'liters')
    get_entry('pounds', 'kilograms')
    get_entry('inches', 'centimeters')
    get_entry('fahrenheit', 'celsius ')


print()


