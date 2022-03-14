class Node:
    def __init__(self, value = None ):
        self.value = value
        self.ref = None

class Singlelinkedlist:
    def __init__(self):
        self.head = None
        
        
    def traverse_LL(self):
        if self.head == None:
            print("Single Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.value)
                n = n.ref
                
ll1 = Singlelinkedlist()
ll1.head = Node(1)
second = Node(2)
third = Node(3)
ll1.head.ref = second
second.ref = third

ll1.traverse_LL()