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
                print(n.data," ", end =" ")
                n = n.ref
    
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while(n.ref != None):
                n = n.ref
            n.ref = new_node
        
ll1 =Linkedlist()
ll1.add_end(10)
ll1.add_end(20)
ll1.add_end(100)
ll1.print__LL()