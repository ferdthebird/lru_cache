
class LruCache:
  """ Least Recently Used Cache

  attributes:  
    max_size: the maximum number of objects in the cache.  After this many objects are in
              cache, the least recently used object will be deleted to make room.
    current_size:  the number of objects currently contained in the cache
    data:  structure where the data objects are stored
  """
  def __init__(self, max_size):
    self.max_size = max_size
    self.current_size = 0
    self.data = CacheData()
    self.hashmap = {}
        
  def fetch(self, key):
    """ returns the value associated with the key if it exists in the cache or None if not"""
    n = self.isInCache(key)

    if n == None:
      return None
    else:
      self.data.moveToFront(n)
      return n.value
    
  def put(self, key, value):
    n = self.isInCache(key)

    if n == None: # not found by fetch
      while self.current_size >= self.max_size:
        deleted_n = self.data.deleteLast()
        self.hashmap[deleted_n.key] = None
        self.current_size -= 1
          
      node=DataNode(key,value)
      self.hashmap[key] = node
      self.data.put(node)
      self.current_size += 1
    else:  # key already exists, overwrite
      n.value = value
      self.data.moveToFront(n)
    
  def isInCache(self, key):
    try:
      node = self.hashmap[key]
      return node
    except KeyError:
      return None

    raise "isInCache: unknown error"

##############################################################################

class CacheData:
  """CacheData:  implements a doubly linked list used to store cache data

  attributes:
    first:  the first object in the list
    last: the last object in the list
  """
  def __init__(self):
    self.first = None
    self.last = None
    
  def dump(self):
    """ dumps the data to stdout """
    current = self.first
    idx=0

    if self.first != None: print("First->%s" % self.first.key),
    if self.last != None: print("Last->%s" % self.last.key),
    print

    while current != None:
      print("index: %d  key: %s  value: %s" % (idx,current.key,current.value)),
      if current.prev != None:
        print ("\tP->%s" % current.prev.key),
      if current.next != None:
        print ("\tN->%s" % current.next.key),
      print
      current = current.next
      idx += 1

  def put(self, n):
    self.push(n)

  def push(self, n):
    """push a node onto the front of the list"""
    if self.first == None: # first node
      self.first = n
      self.last = n
      return

    n.next = self.first
    n.prev = None
    self.first.prev = n
    self.first = n

  def moveToFront(self,n):
    """moves an existing object to the front of the list"""
    if n.prev == None: # it's already first, nothing to do
      return
    else:
      n.prev.next = n.next

    if n.next == None: # last
      self.last = n.prev
      n.prev.next = None
    else:
      n.next.prev = n.prev

    self.first.prev = n
    n.next = self.first
    self.first = n
    self.first.prev = None

  def deleteLast(self):
    """deletes the last object in the list, returns the deleted node so we can update hashmap"""
    rv = self.last
    new_last = self.last.prev
    new_last.next = None;
    self.last = new_last
    return rv

##############################################################################

class DataNode:
  """DataNode:  a doubly linked list key/value data node.

  attributes:
    key:  
    value: 
    next: the next objects in the list or None
    prev: the previous object in the list or None
  """
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None

##############################################################################

