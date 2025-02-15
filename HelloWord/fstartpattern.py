"""following pattern will be printedf
    *****
    **
    *****
    **
    **
"""
# import sys
# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     for y in range(x):
#        sys.stdout.write('*')
#     print('')

fpattern = [5, 2, 5, 2, 2] # for printing F
lpattern = [1, 1, 1, 1, 1, 6] # for printing L 
numbers = lpattern
for x_count in numbers:
    output = ''
    for y in range(x_count):
        output += '*'
    print(output)
       
    