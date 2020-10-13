# Lab 4b: draw an inverted using loops.
# Cassandra Francis

# Size of the first line/number of rows
size = 10

for r in range(size):
    for c in range(size - r, 0, -1):
        print('*', end='')
    print()