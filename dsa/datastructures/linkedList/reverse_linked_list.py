class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def traverseAndPrint(node):
    currentNode = node
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("Null")

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev
    
    
    
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

head = reverseLinkedList(node1)

traverseAndPrint(head)

