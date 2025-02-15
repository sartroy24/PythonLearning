import sys
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    for y in range(x):
       sys.stdout.write('*')
    print('')