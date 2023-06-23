class Node:
  def __init__(self, val, next=None) -> None:
    self.val = val
    self.next = next

def middle_of_linked_list(head):
  slow = fast = head
  '''
  We have to check 'fast' because if list length is odd, 
  the 'fast' pointer would reach the last node. 
  And if list length is even, 
  the 'fast' pointer would land on null.
  '''
  while fast and fast.next:
    fast = head.next.next
    slow = slow.next  
  return slow.val 
