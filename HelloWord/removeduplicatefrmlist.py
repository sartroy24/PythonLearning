# numbers = [5, 6, 1, 5, 9, 10, 33, 12, 10, 55]
# for item in numbers:
#     if numbers.count(item) != 1:
#         numbers.remove(item)
# print(numbers)


numbers = [5, 6, 1, 5, 9, 10, 33, 12, 10, 55]
unique_nums = []
for item in numbers:
    if item not in unique_nums:
        unique_nums.append(item)
print(unique_nums)