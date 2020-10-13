# inverted triangle pattern with * using loops, 10 rows.

# rows = 10  # number of rows/asterisks in top row
# for r in range(rows):  #
#     for c in range(10 - r): # start at 10 * subtract 1 each iteration
#         print('*', end='')  # use * to "draw" triangle
#     print()  # print blank line


for r in range(11, 0, -1):  # range 1-10 with -1 steps
    for c in range(r - 1):  # subtract 1 on each column
        print('*', end='')  # use * to "draw" triangle with no spaces between
    print()  # print blank line
