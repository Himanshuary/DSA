class Queue:
    
    # Creating a queue
    def __init__(self):
        self.queue = []
    
    # check Queue is empty or not 
    # Or Isempty
    def check_empty(self):
        if self.queue == 0:
            return "Queue is empty"
    
    # Add a element in the queue
    # or Enqueue
    def Enqueue(self, value):
        self.queue.append(value)
        
    # Remove a element in the queue
    # Or Dequeue
    def Dequeue(self):
        self.queue.pop(0)
    
    # peek operation return the front element of queue
    
    def peek(self):
        return "Front element of queue: ", self.queue[0]
    
    # Display the queue
    
    def Display(self):
        print(self.queue)

q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Dequeue()
q.Display()
