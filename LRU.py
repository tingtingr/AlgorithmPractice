# import time
# from collections import OrderedDict

# class LRUCache(object):
#     def __init__(self, n):
#         self.n = n
#         self.data = OrderedDict()

#     def set(self, key, value):
#         if len(self.data) >= self.n and key not in self.data:
#             self.evict()
#         if key not in self.data:
#             self.data[key] = (value, time.time())
#         if key in self.data and value != self.data[key][0]:
#             self.data[key] = (value, time.time())
        
#     def get(self, key):
#         if key in self.data:
#             value = self.data.get(key)[0]
#             self.data.update({key:(value,time.time())})
#             return value
#         else:
#             return -1

#     def evict(self):
        
#         x = self.data.popitem(last=True)
#         print(x)


import time
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, n):
        self.n = n
        self.data = OrderedDict()

    def set(self, key, value):
        if key not in self.data:
            if len(self.data) >= self.n:
                self.evict()
            else:
                self.data[key] = value
        if key in self.data:
            self.data.update({key:value})
        
    def get(self, key):
        if key in self.data:
            value = self.data.get(key)
            self.data.update({key:value})
            return value
        else:
            return -1

    def evict(self):
        x = self.data.popitem(last=False)
        print(x)


import heapq
import time
class LRUCache(object):
    def __init__(self,n):
        self.n = n
        self.data = []
        # (time,[key,value])
    def set(self, key, value):
        keys = [x[1][0] for x in self.data]
        if key in keys:  
            # if len(self.data) >= self.n:
            #     heapq.heappushpop(self.data,(time.time(),[key,value]))
            # else:
                index = keys.index(key)
                self.data[index] = (time.time(),[key,value])
        else:
            if len(self.data) >= self.n:
                print("not in keys, pushpop")
                print("least recent one is ")
                heapq.heapify(self.data)
                heapq.heappushpop(self.data,(time.time(),[key,value]))
            else:
                self.data.append((time.time(),[key,value]))
        # else:
        #     if keyn b
        #     self.data.append((time.time(),[key,value]))

    def get(self, key):
        keys = [x[1][0] for x in self.data]
        if key in keys:
            index = keys.index(key)
            value = self.data[index][1][1]
            self.data[index] = (time.time(),[key,value])
            return self.data[keys.index(key)][1][1]
        else:
            return -1
    # def evict(self):
    #     heapq.heapify(self.data)
    #     heapq.heappop(self.data)


# 2,[get(2),set(2,6),get(1),set(1,5),set(1,2),get(1),get(2)]
# 2,[set(2,1),set(1,1),get(2),set(4,1),get(1),get(2)]
# 2,[
# c.get(2),set(2,6),get(1),set(1,5),set(1,2),get(1),get(2)]

c = LRUCache(2)
# 2,[set(2,1),set(1,1),get(2),set(4,1),get(1),get(2)]
print(c.get(2))
print(c.data)
c.set(2,6)
print(c.data)
print(c.get(1))
print(c.data)
c.set(1,5)
print(c.data)
c.set(1,2)
print(c.data)
# print(c.get(2))
# print(c.data)
# c.set(4,1)
# print(c.data)
print(c.get(1))
print(c.data)
print(c.get(2))


# Input:
# 2,[set(2,1),set(2,2),get(2),set(1,1),set(4,1),get(2)]
# Output:
# [1,-1]
# Expected:
# [2,-1]

    # OrderedDict(sorted(L.items() key = lambda t:t[1]))