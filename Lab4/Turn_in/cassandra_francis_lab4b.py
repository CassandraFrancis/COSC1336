# Cassandra Francis Lab 4b
# In this portion of the lab you will draw an inverted triangle using loops. 

rows = 10  # number of rows/asterisks in top row
for r in range(rows):  # 
    for c in range(10 - r): # start at 10 subtract 1 from each column
        print('*', end='')  # use the '*' character to "draw" triangle with no spaces between characters
    print()  # print blank line

print('\nAnother way to get the same results:\n')

for r in range(11, 1, -1):  # range 10-1 with -1 steps
    for c in range(r - 1):  # subtract 1 on each column
        print('*', end='')  # use the '*' character to "draw" triangle with no spaces between characters
    print()  # print blank line
