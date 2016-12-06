class Solution(object):
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        alphaNum = [ i +48 for i in range(10)]+ [j +65 for j in range(26)] + [z + 97 for z in range(26)]
#        print(alphaNum)
        while start < end:
            print(s[start], s[end])
            if s[start] not in alphaNum:
                start += 1
            if s[end] not in alphaNum:
                end -= 1
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True
s = "a."
Solution().isPalindrome(s)