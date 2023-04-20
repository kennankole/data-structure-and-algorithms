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
    
  def insert_after_item(self, item, data):
    new_node = Node(data)
    if self.head:
      current_node = self.head
      while(current_node):
        if item == current_node.data:
          break
        current_node = current_node.next
      if not current_node:
        print('Item not found')
      else:
        new_node.prev = current_node
        new_node.next = current_node.next
        if current_node.next:
          current_node.next.prev = new_node
        current_node.next = new_node
    else:
      print('Empty list')
      
      
  def insert_before_item(self, item, data):
    new_node = Node(data)
    if self.head:
      if self.head.data == item:
        return self.insert_start(data)
      current_node = self.head
      while(current_node.next):
        if current_node.next.data == item:
          break
        current_node = current_node.next
      if not current_node.next:
        print('Item not found')
      else:
        new_node.next = current_node.next
        current_node.next.prev = new_node
        current_node.next = new_node
        new_node.prev = current_node
    else:
      print('Empty list')
      
one = DoubleLinkedList()
one.insert_start(40)
one.insert_start(250)
one.insert_end(600)
one.insert_after_item(600, 500)
one.insert_before_item(250, 4000)
one.print_list()
  