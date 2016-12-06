class Solution(object):
    def isMatch(self, s, p):
        self.removeStar(p)
        if len(p) == 2 and p[0] == '.' and p[1] == '*':
            return True
        if s == "" or p =="":
            if len(p) == 2 and p[1] == "*":
                return True
        row = len(s)
        col = len(p)
        dp = [[False for i in range(col + 1)] for j in range(row + 1)]
        dp[0][0] = True

        for i in range(1,col):
            if p[i] == '*':
                dp[0][i+1] = dp[0][i-1]

        self.printMatrix(dp)
        print('finished init')
        for i in range(row):
            for j in range(col):
                cur = p[j]
                print(i,j)
                print(cur)
                if cur == '*':
                    if p[j - 1] != '.':
                        dp[i+1][j+1] = dp[i][j] and s[i] == s[i-1] or dp[i+1][j - 1] or dp[i+1][j]
                        print("pre is .")
                    else:
                        dp[i+1][j+1] = dp[i][j] or dp[i+1][j - 1] or dp[i+1][j] or dp[i][j + 1]
                        self.printMatrix(dp)
                elif cur == '.':
                    print("now cur is .")
                    dp[i+1][j+1] = dp[i][j]
                else:
                    print("now cur is char")
                    dp[i+1][j+1] = dp[i][j] and s[i] == p[j]
            self.printMatrix(dp)
        return dp[-1][-1]



    def removeStar(self, p):
        a = [i for i in p]
        i = 0
        while i < len(a) - 1 > 0:
            if a[i] == '*' and a[i+1] == '*':
                del a[i+1]
            else:
                i += 1
        return "".join(a)

    def printMatrix(self, m):
        col = len(m[0])
        row = len(m)
        for i in range(row):
            for j in range(col):
                print("%2d" % (m[i][j])),
            print("\b")
        print("\n")

# s="aaa"
# p=".*"


s="bbbba"
p=".*a*a"
print(Solution().removeStar(p))
print(Solution().isMatch(s,p))