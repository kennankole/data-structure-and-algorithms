


class Node:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.head != None:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node

    def inserting(self, data):
        new_node = Node(data)
        if self.head:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next 
            current_node.next = new_node
        else:
            self.head = new_node

    def display(self):
        current_node = self.head 
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            

llist = LinkedList()
llist.inserting(25)
llist.inserting(40)
llist.inserting(2)
llist.inserting(10)
llist.display()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    