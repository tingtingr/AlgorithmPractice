import sys
class Solution(object):
    def findLadders(self, s1, s2, words):
        res = []
        alpha = [chr(x) for x in range(ord('a'), ord('a')+26)]
        if s1 in words:
            words.remove(s1)
        if s2 in words:
            words.remove(s2)
        self.helper(res, s1, s2, [s1], words, alpha)
        return res
    def helper(self, res, s1, s2, sub, words, alpha):
        print(sub, words)
        print('\n')
        # if len(res) != 0:
        maxl = sys.maxsize
        if len(res) != 0:
            print("res length not equal to zero")
            maxl = len(res[0])
        if self.dif(sub[-1], s2) and len(sub) <= maxl -1 :
            res.append(sub + [s2])
        lastword = sub[-1]
        x = words
        newlevel = self.getlist(lastword, x, alpha)
        print('newlevel')
        print(newlevel)
        for w in newlevel:
            self.helper(res, s1, s2, sub+[w], x, alpha)
            
    def dif(self, s1, s2):
        cnt = 0
        for i in range(len(s1)):
            if cnt > 1:
                return False
            if s1[i] != s2[i]:
                cnt += 1
        return cnt == 1
        
    def getlist(self, s, words, alpha):
        res = []
        for i in range(len(s)):
            candidates = [s[:i] + a + s[i + 1:] for a in alpha if a != s[i]]
            for c in candidates:
                if c in words:
                    res.append(c)
                    words.remove(c)
        return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]


beginWord ="a"
endWord = "c"
wordList = ["a","b","c"]



beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog","dot"]



beginWord = "hot"
endWord = "dog"
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]


beginWord = "hit"
endWord = "cog"
wordList = ["hot","cog","dot","dog","hit","lot","log"]

print(Solution().findLadders(beginWord,endWord,wordList))