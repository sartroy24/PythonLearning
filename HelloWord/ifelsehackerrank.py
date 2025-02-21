number = int(input('Enter the number: '))
def check_even(value):
    return number % 2 == 0

if not check_even(number):
    print("Weird")
elif check_even(number) and (2 <= number <= 5):
    print("Not weird")
elif check_even(number) and (6 <= number <= 20):
    print("Weird")
elif check_even(number) and number > 20:
    print("Not weird")

