class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
    def insert(self, data):
        # insert from front
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        # insert from back
        new_node = Node(data)
        anchor = self.head
        while self.head.next_node:
            self.head = self.head.next_node
        self.head.next_node = new_node
        self.head = anchor
    def size(self):
        cur = self.head
        count = 0
        while cur:
            count +=1 
            cur = cur.get_next()

class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList(object):
    def __init__(self,nums):
        self.head= ListNode(0)

    def fromList(self,nums):
        cur = self.head
        for x in nums:
            cur = ListNode(x)
            cur = cur.next
        self.printLinkedList()

    def printLinkedList(self):
        cur = self.head
        print(cur,self.head)
        while cur:
            print(cur.val),
            if cur.next:
                print("->") 
            cur = cur.next

nums= [1,2,3]