class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        n = self.head
        if n is None:
            print("Linked list is empty")
        else:
            while n is not None:
                print(n.value,end = " ")
                n = n.next
    # Insert element beginning of the Linked List
    def add_begin(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    # Insert element end of the Linked List
    def add_end(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = newNode
            
    def add_after(self,value,x):
        n = self.head
        while n is not None:
            if x == n.value:
                break
            n= n.next
        if n is None:
            print("The node is not present in Linked List")
        else:
            newNode = Node(value)
            newNode.next = n.next
            n.next = newNode
            
SLL1 = Slinkedlist()
SLL1.add_begin(10)
SLL1.add_begin(20)
SLL1.add_end(110)
SLL1.add_begin(5)
SLL1.add_after(69,20)
SLL1.print_LL()