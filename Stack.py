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
    


