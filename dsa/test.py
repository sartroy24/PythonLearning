def counting_sort(arr):
    if not arr:
        return []

    max_value = max(arr)
    count = [0] * (max_value + 1)  

    # Step 1: Count occurrences
    for num in arr:
        count[num] += 1

    # Step 2: Modify count array for positions
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 3: Build the sorted output array
    output = [0] * len(arr)
    for num in reversed(arr):  # Reverse to maintain stability
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Example Usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)
