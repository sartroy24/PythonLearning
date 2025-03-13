def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value+1)
    
    for num in arr:
        count[num] += 1
        
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]
        
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output


# Example Usage
arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)