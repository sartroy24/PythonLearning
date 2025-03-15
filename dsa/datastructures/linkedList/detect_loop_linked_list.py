class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectLoop(head):
    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          return True
    return False
            
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

# traverseAndPrint(node1)
print('Loop detected', detectLoop(node1))