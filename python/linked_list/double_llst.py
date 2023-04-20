class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    
class DoubleLinkedList:
  def __init__(self):
    self.head = None
    
  def print_list(self):
    if self.head:
      current_node = self.head
      while(current_node):
        print(current_node.data)
        current_node = current_node.next
    
  def insert_start(self, data):
    new_node = Node(data)
    if self.head:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node
  
  def insert_end(self, data):
    new_node = Node(data)
    if self.head:
      current_node = self.head
      while(current_node.next):
        current_node = current_node.next
      current_node.next = new_node
      new_node.prev = current_node
    else:
      return self.insert_start(data)
      
one = DoubleLinkedList()
one.insert_start(40)
one.insert_start(250)
one.insert_end(600)
one.print_list()
      
  