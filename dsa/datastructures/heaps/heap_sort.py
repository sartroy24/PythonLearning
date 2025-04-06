#Heap Sort
# Time: O(n log n), Space: O(n)
# NOTE: O(1) Space is possible via swapping, but this is complex

import heapq
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    
    for i in range(n):
        new_list[i] = heapq.heappop(arr)
    
    return new_list

print('sorted array',heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))