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
                 



                 
                 
                 
                 
                 
