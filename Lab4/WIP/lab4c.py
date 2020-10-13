# Read in a numeric grade from a student
# Convert numeric grade to a letter grade
# Keep a running total of grades entered
# Keep a count of the number of grades entered
# Issue a message about the grade (you passed, you failed etc.)
# At the end calculate class average unless there were no grades entered
# Output will include: the individual grades converted, the message to student, class average, number of grades entered

# variables and initial values
grade = float(0)
total_grade = float(0)
num_entries = int(0)

# get input, numerical grade
grade = float(input('Please enter your numerical grade: '))

# while loop, use -1 to break loop, convert numerical grade to letter grade w/ message
while grade != -1:  # while grade entered is not -1
    if grade >= 90:  # 100+ to 90 is an A
        print('Great job! You earned an A!')
    elif 90 > grade >= 80:  # 89 to 80 is a B
        print('You earned a B, nice work!')
    elif 80 > grade >= 70:  # 79 to 70 is a C
        print('You passed with a C!')
    elif 70 > grade >= 60:  # 69 to 60 is a D
        print('You earned a D. Let\'s work on studying more!')
    else:  # less than 60 is a F
        print('You earned an F. Let\'s figure out where you went wrong')
    num_entries += 1  # add 1 to number of entries (running total)
    total_grade += grade  # add grade tot total grade (running total)
    grade = float(input('Enter your next grade, or -1 to end the program: '))  # enter next grade or end program
if num_entries > 0:  # if at least 1 entry get average grade
    average = total_grade / num_entries  # calculations class average
    print('Based on the ', num_entries, ' grades entered, your class average is ', format(average, '.2f'))  # display number of grades entered and class avg
