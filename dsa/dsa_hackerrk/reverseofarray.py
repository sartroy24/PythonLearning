arr = [1, 2, 3]

def reverseArray(a):
    reverseArr = []
    for i in range(len(a) - 1, -1, -1):
        reverseArr.append(a[i])
    return reverseArr
    
print('Reverse of Array:', reverseArray(arr))