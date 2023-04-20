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
    else:
      print('Empty list')
    
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
    if not self.head:
      print('Empty list')
    else:
      current_node = self.head.next
      if current_node:
        current_node.prev = None
      self.head = current_node
      
  def delete_end(self):
    if not self.head:
      print('Empty list')
    if not self.head.next:
      self.head = None
    current_node = self.head
    while current_node.next:
      current_node = current_node.next
    current_node.prev.next = None
    
  def delete_by_value(self, item):
    if not self.head:
      print('Emtpy list')
  
    if self.head.data == item and self.head.next == None:
      self.head = self.head.next
    elif self.head.data == item and self.head.next != None:
      self.head = self.head.next
      self.head.prev = None
    else:
      current_node = self.head
      while current_node:
        if item == current_node.data:
          break
        current_node = current_node.next
      if not current_node:
        print('Item not found')
      else:
        if current_node.next:
          current_node.prev.next = current_node.next
          current_node.next.prev = current_node.prev
        else:
          current_node.prev.next = None
    
  def reverse(self):
    current_node = self.head
    while current_node:
      temp = current_node.prev
      current_node.prev = current_node.next
      current_node.next = temp
      current_node = current_node.prev
    if temp:
      self.head = temp.prev
      
  def search_by_value(self, item):
    if not self.head:
      print('Empty list')
    else:
      current_node = self.head
      while(current_node):
        if item == current_node.data:
          print("Found it",current_node.data)
          break
        current_node = current_node.next
      if not current_node:
        print('Item not found')
  
  def search_by_index(self, position):
    if not self.head:
      print('Empty list')
    elif position == 0:
      print(self.head.data)
    else:
      current_node = self.head
      index = 0
      while (current_node and index < position):
        index += 1
        current_node = current_node.next
      if not current_node:
        print('Index out of range')
      else:
        print("Found it here:",current_node.data)
      
one = DoubleLinkedList()
one.insert_start(40)
one.insert_start(250)
one.insert_end(600)
one.insert_after_item(600, 500)
one.insert_before_item(250, 4000)
one.insert_at_index(2, 45)
one.print_list()
print()
one.reverse()
one.search_by_index(3)
one.print_list()
  