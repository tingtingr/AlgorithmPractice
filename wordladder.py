# class Solution(object):
#     def ladderLength(self, s1, s2, words): 
#         if s1 == s2:
#             return 1
#         alpha = [chr(x) for x in range(ord('a'),ord('a')+26)]
#         queue = []
#         queue.append([s1])
#         length = 2
#         while queue:
#             temp = queue.pop()
#             print(temp)
#             for s in temp:
#                 # print(s,s2)
#                 if s in words:
#                     words.remove(s)
#                 if self.helper(s, s2):
#                     return length
#                 else:
#                     level = []
#                     # print("not the same")
#                     for i in range(len(s)):
#                         candidates = [s[:i] + a + s[i + 1:] for a in alpha if a != s[i]]
#                         for c in candidates:
#                             if c in words:
#                                 # print('found')
#                                 level.append(c)
#                                 words.remove(c)
#                     queue.insert(0,level)
#                     print('level'),
#                     print(level)
#                     print(length)
#             length += 1
#         return 0

#     def helper(self,s1,s2):
#         count = 0
#         for i in range(len(s1)):
#             if count > 1:
#                 return False
#             if s1[i] != s2[i]:
#                 count += 1
#         return count < 2

class Solution(object):
    def ladderLength(self, s1, s2, words): 
        if s1 == s2:
            return 1
        alpha = [chr(x) for x in range(ord('a'),ord('a')+26)]
        queue = []
        queue.append([s1])
        length = 2
        while queue:
            temp = queue.pop()
            for i in temp:
                print(temp,i)
                if self.helper(i,s2):
                    return length
            newlevel = self.getlist(temp, words, alpha)
            if len(newlevel) > 0:
                queue.append(newlevel)
                print(newlevel, length)
                length += 1
            else:
                break
        return 0
    def helper(self,s1,s2):
        count = 0
        for i in range(len(s1)):
            if count > 1:
                return False
            if s1[i] != s2[i]:
                count += 1
        return count < 2
        
    def getlist(self, l, words, alpha):
        res = []
        for s in l:
            for i in range(len(s)):
                candidates = [s[:i] + a + s[i+1:] for a in alpha if a!= s[i]]
                for c in candidates:
                    if c in words:
                        res.append(c)
                        words.remove(c)
        print(res)
        return res

s1="hit"
s2="cog"
words=["hot","cog","dot","dog","hit","lot","log"]
words=["hot","dot","dog","lot","log"]
s1="leet"
s2="code"
words=["lest","leet","lose","code","lode","robe","lost"]
# s1 ="kiss"
# s2 = "tusk"
# words = ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]
s1= "hot"
s2 = "dog"
words= ["hot","dog"]
print(Solution().ladderLength(s1,s2,words))