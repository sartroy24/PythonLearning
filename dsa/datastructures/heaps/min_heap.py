#Build Min Heap(heapify)
#Tine: O(n), Space: 0(1)
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)

print('Created heap: ', A)

# Heap push (Insert Element)
# Time: O(log n)

heapq.heappush(A, 4)

print('Updated Heap: ', A)

# Heap pop (Extract min)
# Time: O(log n)

minn = heapq.heappop(A)

print('min value: ', minn)
print('Updated Heap: ', A)