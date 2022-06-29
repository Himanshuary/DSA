class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head
            while(n!=None):
                print(n.data)
                n = n.ref

    def LL_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

ll1 = Linkedlist()
ll1.LL_empty(20)
ll1.LL_empty(200)

ll1.print_LL()