class TreeNode(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
class Tree(object):
    def __init__(self,val):
        self.root = TreeNode(val)



def serialize(root):
    res = []
    level = [root]
    while level:
        for i in level:
            if isinstance(i,TreeNode):
                res.append(i.val)
            else:
                res.append(i)
        pairs = [(x.left,x.right) for x in level if isinstance(x,TreeNode)]
        temp = []
        for p in pairs:
            for y in p:
                if y:
                    temp.append(y)
                    # res.append(y.val)
                else:
                    temp.append('#')
                    # res.append('#')
        cnt = 0
        for x in temp:
            if x != '#':
                cnt += 1
        if cnt == 0:
            level = []
        else:
            level = temp
        # print(level)
    print(res)
    return res

def deserialize(data):
    levels = []
    cnt = 0
    def construct(parents, children):
        res = []
        # print(parents,children)
        for i in range(len(parents)):
            nodei = TreeNode(parents[i])
            nodei.left = children[2*i] if children[2*i] != '#' else None
            nodei.right = children[2*i + 1] if children[2*i+1] !='#' else None
            res.append(nodei)     
        return res
    while data:
        level = list(data[:2**cnt])
        data = data[2**cnt:]
        levels.append(level)
        cnt += 1
    # print(levels)
    
    i = len(levels) - 1
    while i > 0:
        x = construct(levels[i-1], levels[i])
        levels[i-1] = x
        i -= 1
    # print(type(levels[0]))
    # print(type(levels[0][0]))
    
    serialize(levels[0][0])
    return levels

tree = Tree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.right.left = TreeNode(4)
tree.root.right.right = TreeNode(5)




y = serialize(tree.root)
print(type(type(tree.root)))
deserialize(y)