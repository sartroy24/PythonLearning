# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
my_array = [7, 3, 9, 12, 11]

N = len(my_array)

for i in range(N):
    swapped = False
    for j in range(N-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted Array: ", my_array)            