MAX_HASH_TABLE_SIZE = 1024

class BasicHashTable:
  def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
    self.data_list = [None] * max_size
    
  def _hash(self, key):
    return abs(hash(key)) % len(self.data_list)
  
  def __setitem__(self, key, value):
    index = self._hash(key)
    self.data_list[index] = (key, value)
    
  def __getitem__(self, key):
    index = self._hash(key)
    if self.data_list[index] != None:
      return self.data_list[index][1]
    else:
      return None
    
  def __iter__(self):
    return (x for x in self.data_list if x is not None)
  
  def __repr__(self):
    from textwrap import indent
    pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
    return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
  
  def __str__(self):
   	return repr(self)
	
table = BasicHashTable()
table['a'] = 1
table['b'] = 34
table['a'] = 99
table['c'] = 70
table['d'] = 80
print(table)