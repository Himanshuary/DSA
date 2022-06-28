class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None  

class Linkedlist:
    def __init__(self):
        self.head = None
    "Traversal Operation"    
    def print__LL(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head
            while (n!=None):
                print(n.data,"", end=" ")
                n = n.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while(n.ref != None):
                n = n.ref
            n.ref = new_node 
            
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
        

ll1 = Linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_begin(40)
ll1.add_begin(50)
ll1.add_end(69)
ll1.add_after(666,30)
ll1.print__LL()