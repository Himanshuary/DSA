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
                print(n.data)
                n = n.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

ll1 = Linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_begin(40)
ll1.add_begin(50)
ll1.print__LL()