class Node:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_end(self, data):
        new_node = Node(data)
        if self.head != None:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node

    def display(self):
        current_node = self.head 
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def insert_middle(self):
        size = self.get_size()
        if (size % 2 == 0):
            mid_point = size / 2
        else:
            mid_point = (size+1) / 2
        return mid_point
            
    def search(self, data):
        current_node = self.head 
        while current_node:
            if data == current_node.data:
                return f"Node found {current_node.data}"
            current_node = current_node.next
        return "Not found"
    
    def get_size(self):
        current_node = self.head
        count = 0
        while current_node:
            count+= 1
            current_node = current_node.next 
        # print(count)
        return count
            
            
    def delete_end(self):
        current_node = self.head 
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        

            

llist = LinkedList()
llist.insert_end(25)
llist.insert_end(40)
llist.insert_end(2)
llist.insert_end(10)
llist.display()
print()
llist.insert_start(5)
llist.display()
print()
llist.insert_start(3)
llist.insert_end(79)
llist.display()
print("Printing th size of the linkedlist")
llist.get_size()
print()
print(llist.insert_middle())

llist.delete_end()
llist.display()
print()
llist.delete_end()
llist.display()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    