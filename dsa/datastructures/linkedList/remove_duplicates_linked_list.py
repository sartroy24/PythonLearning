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

def removeDuplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
    
node1 = Node(2)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

head = removeDuplicates(node1)

traverseAndPrint(head)