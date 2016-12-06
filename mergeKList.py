import heapq
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        res = []
        print("printlist")
        self.printList(lists[0])
        self.printList(lists[1])
        for i in range(len(lists)):
            print("print val")
            print(lists[i].val)
            if lists[i] is None:
                continue
            heapq.heappush(heap, (lists[i].val, i))
        print(heap)
        
        while len(heap) != 0:
            root = heap[0]
            print("root")
            print(root)
            heapq.heappop(heap)
            res.append(root[0])
            index = root[1]
            if lists[index].next:
                heapq.heappush(heap, ( lists[index].next.val, index))
                lists[index] = lists[index].next
                
                print("after push")
                print(heap)
        print(res)
        return res
    def printList(self, head):
        while head:
            print(head.val),
        
            head = head.next
        print("\b")
            
head1 = ListNode(1)
head2 = ListNode(3)
head1.next = ListNode(2)
head2.next = ListNode(4)
#print(head1)
#print(head2)
sample = []
sample.append(head1)
sample.append(head2)
Solution().mergeKLists(sample)
