class Node():
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None, None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        # Left = LRU, right = most recently used
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
        
    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

