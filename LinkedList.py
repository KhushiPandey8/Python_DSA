#Traversal On Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def traverse(head):
        current = head
        while current is not None:
            print(current.data)
            current = current.next
        print("null")
Node1 = Node(10)
Node2 = Node(20)   
Node3 = Node(30)
Node4 = Node(40)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node.traverse(Node1)


#Find The Lowest Number In Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def findLowest(head):
        minVal = head.data
        current = head
        while current is not None:
            if current.data < minVal:
                minVal = current.data
            current = current.next
        return minVal
Node1 = Node(10)
Node2 = Node(5)   
Node3 = Node(11)
Node4 = Node(40)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
print("Lowest Number In Linked List :" ,Node.findLowest(Node1))

#Delete A Node In Linked List
