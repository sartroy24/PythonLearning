numbers = [7, 10, 1, 3, 5, 9, 10, 50, 1, 80]
largest = numbers[0]
for item in numbers:
    if item > largest:
        largest = item
print(f'The largest number is {largest}')