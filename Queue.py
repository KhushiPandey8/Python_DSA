queue = []

#Enqueue Op
queue.append(1)
queue.append(3)
queue.append(5)
queue.append(7)
queue.append(9)
print("Queue Numbers :",queue)

#Peek Op

frElement = queue[0]
print("Peeked Number :" ,frElement)

#Pop Op (Dequeue)
poppedElement = queue.pop(0)
print("Dequeued Number :" ,poppedElement)

print("After Dequeue Elements Are :" ,queue)

#isEmpty
isEmpty = len(queue) == 0
print("Is the queue empty? ", isEmpty)

print("Size of the queue is: ", len(queue))







