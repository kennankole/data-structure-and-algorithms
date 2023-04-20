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
      
  def insert_at_index(self, position, item):
    new_node = Node(item)
    if self.head:
      if position == 0:
        return self.insert_start(item)
      current_node = self.head
      index = 0
      while (current_node and index < position - 1):
        index += 1
        current_node = current_node.next
      new_node.next = current_node.next
      new_node.prev = current_node
      current_node.next.prev = new_node
      current_node.next = new_node
    else:
      print('Empty list')
      
  def delete_start(self):
    if self.head:
      if not self.head.next:
        self.head = None
      self.head = self.head.next
      self.head.prev = None
    else:
      print("Empty list")
      

      
one = DoubleLinkedList()
one.insert_start(40)
one.insert_start(250)
one.insert_end(600)
one.insert_after_item(600, 500)
one.insert_before_item(250, 4000)
one.insert_at_index(2, 45)
one.print_list()
print()
one.delete_start()
one.print_list()
  