def merge(left, right):
    sorted_array = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array


def merge_sort_iterative(arr):
    length = len(arr)
    width = 1
    
    while width < length:
        for i in range(0, length, 2 * width):
            left = arr[i : i+width]
            right = arr[i+width : i + 2 * width]
            merged_array = merge(left, right)
            arr[i: i + 2 * width] = merged_array
        width *= 2
    
    return arr


arr = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_arr = merge_sort_iterative(arr)
print("Sorted array:", sorted_arr)