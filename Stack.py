#Stack Implementation using list

stack = []

#Push
stack.append(1)
stack.append(3)
stack.append(34)
stack.append(23)
stack.append(56)
stack.append(21)
stack.append(0)

print("Stack: ", stack)

#Peek

topElement = stack[-1]
print("Top element in the stack is: ", topElement)

#Pop
popElement = stack.pop()
print("Popped element is:", popElement)

#Empty Stack

isEmpty = len(stack) == 0
print("Is the stack empty? ", isEmpty)

isEmpty_two = not bool(stack)
print("Is the stack empty? ", isEmpty_two)

#Size of the stack
stackSize = len(stack)
print("Size of the stack is: ", stackSize)



#Creating a stack using Class

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,  val):
        self.stack.append(val)
    
    def pop(self):
       if self.IsEmpty():
            return "stack is empty"
       return self.stack.pop()
    
    def peek(self):
        if self.IsEmpty():
            return "stack is empty"
        return self.stack[-1]
     
    def IsEmpty(self):
        return len(self.stack) == 0

    def Size(self):
        return len(self.stack)
    

StackClass = Stack()

StackClass.push(3)
StackClass.push(4)
StackClass.push(6)
StackClass.push(14)

print("Stack :" ,StackClass.stack)
print("Peek :",StackClass.peek())
    


# Stack Implementation using Linked Lists

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.size += 1
    def pop(self):
        if self.IsEmpty():
            return "Stack is empty"
        poppedNode = self.head
        self.head = self.head.next
        self.size -= 1
        return poppedNode.val
    def  peek(self):
        if self.IsEmpty():
            return "Stack is empty"
        return self.head.val
    def IsEmpty(self):
        if self.size == 0:
            return True
        return False
    def Size(self):
        return self.size
    def triverse(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.val, end=" ")
            currentNode = currentNode.next
        print()

MyStack = Stack()
MyStack.push(2)
MyStack.push(1)
MyStack.push(5)
MyStack.push(7)
MyStack.push(23)

print("Stack LinkedList: ", end="")
MyStack.triverse()
print("Pop: ", MyStack.pop())
