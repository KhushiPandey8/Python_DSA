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