from multiprocessing import current_process


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
    
    def insert_after_item(self, item, data):
        new_node = Node(data)
        current_node = self.head 
        while current_node:
            if current_node.data == item:
                break
            current_node = current_node.next 
        if current_node is None:
            print("No item in the linked list")
        else:
            new_node.next = current_node.next 
            current_node.next = new_node
        
    
    def insert_before_an_item(self, item, data):
        if self.head is None: # Check if the list is empty
            print("List is empty")
        # Check if the item exists in the first index 
        # of the linked list
        if self.head.data == item:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node 
        # Item does not exist in the first index
        current_node = self.head
        while current_node.next:
            if current_node.next.data == item:
                break
            current_node = current_node.next
        if current_node.next is None:
            print("Item not in the list")
        else:
            new_node = Node(data)
            new_node.next = current_node.next 
            current_node.next = new_node
        
            
        

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
        return count
            
            
    def delete_end(self):
        current_node = self.head 
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        
    def delete_start(self):
        self.head = self.head.next
            
print('----++++++------')
llst = LinkedList()
llst.insert_start(60)
llst.insert_start(80)
llst.display()
print('----++++++------')
llst.insert_end(5)
llst.insert_end(3)
llst.display()
print('----++++++------')
llst.insert_after_item(5, 450)
llst.display()
print('----++++++------')
llst.insert_before_an_item(5, 333)
llst.display()
print('----++++++------')

                 



                 
                 
                 
                 
                 
