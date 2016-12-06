import sys

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, child):
        if child.val < self.val:
            if self.left:
                self.left.insert(child)
            else:
                self.left = child
        else:
            if self.right:
                self.right.insert(child)
            else:
                self.right = child
    def _insert(self, root, node):
        if root is None:
            return node
        if node.val > root.val:
            return self.insert(root.right, node)
        else:
            return self.insert(root.left, node)

class Solution(object):
    def morrisInOrder(self, root):
        cur = root
        i = 0
        while cur is not None:
#        left is None since it is inorder, we have finished the left, so we could
#        visit the current node and go to its right
            if cur.left is None:
                print("left is None"),
                print('%d(%d)'%(cur.val,i))
                cur = cur.right
                i+=1
#        left is NOT None
            else:
                predecessor = cur.left
#                pre.right make sure it goes to the right most,
#                pre.right != cur make sure we could analyse the following condition 
#                and remove the trackback
                while predecessor.right is not None and predecessor.right is not cur:
                    predecessor = predecessor.right
#                    if not visited before, then set the trackback and keep going down the tree
                if predecessor.right is None:
                    predecessor.right = cur
                    print("predecessor.right is None")
                    print(cur.val)
                    print('<-(%d)'%i)
                    cur = cur.left
                    i+=1
#                    if predecessor.right == cur, we have visited all the left node 
#                    this is the second time we are at cur, then we should 
                else:
                    predecessor.right = None
                    print("predecessor.right is cur")
                    print('%d(%d)'%(cur.val,i))

                    cur = cur.right
                    i+=1

    def morrisPreOrder(self, root):
        cur = root
        while cur is not None:
            if cur.left is None:
                print(cur.val)
                cur = cur.right
            else:
                predecessor = cur.left
                while predecessor.right != cur and predecessor.right is not None:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = cur
                    print(cur.val)
                    cur = cur.left
                else:
                    predecessor.right = None
                    cur = cur.right


def array_to_tree(a):
    if not a:
        return None
    root = Node(a[0])
    for val in a[1:]:
        root.insert(Node(val))
    return root

if __name__ == '__main__':
    if len(sys.argv) < 2:
        vals = [7,6,8,5,9,4,10]
    else:
        vals = [int(x) for x in sys.argv[1].split(' ')]
    root = array_to_tree(vals)
    Solution().morrisInOrder(root)

#arr = [1,None,2,3]
#print(a.val)
#print(a.left.val)
#print(a.right.val)
#print("\t in order \t")
#Solution().morrisInOrder(a)
#print("\t pre order \t")
#Solution().morrisPreOrder(a)