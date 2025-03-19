queue = []

#enqueue
queue.append('A')
queue.append('B')
queue.append('C')

#dequeue
element = queue.pop(0)
print("Dequeue: ", element)

#peek
frontElement = queue[0]
print("Peek: ", frontElement)

#isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

#Size
print("Size: ", len(queue))
