# Cassandra Francis - Lab 4c
# You are the professor for COSC 1336 at Austin Community College.  You want to write a program that will take in the number of grades of the students in your class.  
# Since the students in a class vary from semester to semester, there is no fixed number assigned to the number of students.  
# You will keep track of how many students’ grade you input.  You will stop taking input when the student enters a grade of minus 1 (-1).

# Your program will use loops and will accomplish the following:
# 1.	Read in a numeric grade from a student
# 2.	Convert the numeric grade to a letter grade using the grade policies in your syllabus.
# 3.	Keep a running total of the numeric grades entered.
# 4.	Keep a count of the number of grades entered.
# 5.	Issue a message that comments on the letter grade earned.  As an example, you may write “You made an F! Obviously you did not study!”
# All input to the program will be interactive from the keyboard.  
# The output of the program will include the individual grades converted, the message issued to the student, a class average, and the number of grades entered.


# variables and initial values
grade = float(0)
totalGrade = float(0)
numEntries = int(0)

# get input; numerical grade
grade = float(input('Please enter your numerical grade: '))

# while loop; use -1 to break loop, convert numerical grade to letter grade w/ message
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

    numEntries += 1  # add 1 to number of entries (running total)
    totalGrade += grade  # add grade to total grade (running total)
    grade = float(input('Enter your next grade, or -1 to end the program: '))  # user input; next grade or -1 end program

if numEntries > 0:  # if at least 1 entry get average grade
    average = totalGrade / numEntries  # calculation for class average
    print('Based on the', numEntries, 'grades entered, your class average is', format(average, '.2f'))  # display number of grades entered and class avg
else:
    print('You must enter at least one grade. Restart the program to enter your grade(s).')  # message if user does not enter any grades
