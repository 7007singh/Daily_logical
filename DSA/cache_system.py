class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):

        next_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self._remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self.remove(lru)

            del self.cache[lru.key]


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
            return
        insert = Node(key, value)
        self._add_to_front(insert)
        self.map[key] = insert
        if len(self.map.keys()) > self.capacity:
            del self.map[self.tail.prev.key]
            self._remove(self.tail.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)