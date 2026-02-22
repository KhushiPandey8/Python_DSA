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



#Python Class using Queue

class Queue:
   def __init__(self):
      self.queue = []
   def enqueue(self , val):
       self.queue.append(val)
   def deueue(self):
       if(len(self.queue) == 0):
           return "Queue is Empty"
       return self.queue.pop(0)
   def peek(self):
       if(len(self.queue) == 0):
           return "Queue is Empty"
       return self.queue[0]
   def isEmpty(self):
       return len(self.queue) == 0
   def size(self):
       return len(self.queue)
   
QueueObj  = Queue()
QueueObj.enqueue(3)
QueueObj.enqueue(45)
QueueObj.enqueue(21)
QueueObj.enqueue(67)
QueueObj.enqueue(89)
print("Queue Numbers :",QueueObj.queue)
print("Peeked Number :" ,QueueObj.peek())   


#Implementing Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
            self.size += 1  
            return
        else:
            self.rear.next = newNode
            self.rear = newNode
            self.size += 1
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.front.data
    def isEmpty(self):
        return self.size == 0   
    def size(self):
        return self.size
    def display(self):
        isEmpty = self.isEmpty()
        if self.isEmpty():
            return "Queue is Empty"
        cur = self.front
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()
QueueObj = Queue()
QueueObj.enqueue(10)
QueueObj.enqueue(3)
QueueObj.enqueue(45)
QueueObj.enqueue(21)
QueueObj.enqueue(67)
QueueObj.enqueue(89)
QueueObj.display()

print("Peeked Number :" ,QueueObj.peek())   
