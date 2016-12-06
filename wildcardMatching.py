class Solution(object):
    def isMatch(self, s, p):
        if s == "" and (p == "*" or p == ""):
#           print("empty")
            return True
        if p == "" and s is not "":
            return False
        row = len(s)
        col = len(p)
        count = 0
        for i in range(col):
            if p[i] == '*':
                # print("*haha")
                count += 1
        if col - count > row:
            return False
        dp = [[False for i in range(col + 1)] for j in range(row + 1)]
        dp[0][0] = True

        if p[0] == '*':
            print("let me pass it")
            for i in range(row + 1):
                dp[i][1] = True 

        for x in range(1, col):
            # print("hey ")
            if dp[0][x] == True and p[x] == '*':
                # print("ohla hey")
                dp[0][x + 1] = True

        if p[0] == '?':
            dp[1][1] = True
        if p[0] is not '?' and p[0] is not '*':
            print("char match")
            if s[0] == p[0]:
                print("char match")
                dp[1][1] = True
        self.printMatrix(dp)

        for i in range(1, row + 1):
            for j in range(2, col + 1):
                cur = p[j - 1]
                print(i,j)
                if cur == '*':
                    print("this is *"),
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]
                    print(dp[i][j])
                elif cur == '?':
                #   print("?")
                    print("this is ?"),
                    dp[i][j] = dp[i - 1][j - 1]
                    print(dp[i][j])
                else:
                    print("this is char"),
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
                    print(dp[i][j])
                self.printMatrix(dp)
        return dp[-1][-1]

    def printMatrix(self, matrix):
        col = len(matrix[0])
        row = len(matrix)
        for i in range(row):
            for j in range(col):
                print("%2d" % (matrix[i][j],)),
            print("\b")
        print("\n")

s= "ho"
p = "**ho"
print(Solution().isMatch(s,p))