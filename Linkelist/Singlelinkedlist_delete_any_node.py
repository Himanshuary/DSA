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
    
    def delete_any_node(self,x):
        if self.head is None:
            print("LL is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in LL")
        else:
            n.ref = n.ref.ref

ll1 = Linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_begin(40)
ll1.add_begin(50)
ll1.delete_any_node(30)
ll1.delete_any_node(100)
ll1.delete_any_node(50)
ll1.print__LL()