class Node(object):
	def __init__(self, val=None):
		self.data = val
		self.pre = None
		self.next = None

class DoublyLinkedList(object):
	def __init__(self, val=None):
		self.head = Node(val)
		self.tail = self.head

	def add(val):
		node = Node(val)
		node.pre = self.tail
		self.tail.next = node
		self.tail = self.tail.next

d = DoublyLinkedList()
d.add(1)
d.add(2)
d.add(3)