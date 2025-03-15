def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #Step 1: Split the array in half
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    #Step 2: Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0
    
    #Comparing the elements in the sub arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    #Adding the remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array


# Example usage
my_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(my_array)
print("Sorted array:", sorted_array)
    