class Solution(object):
    def LCS(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        if len1 == 0 or len2 == 0:
            return 0
        dp = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
        self.printMatrix(dp)
        for i in range(len2):
            print("for row {0}".format(i))
            self.printMatrix(dp)
            for j in range(len1):
                maX = max(dp[j + 1][i], dp[j][i + 1])
                if str1[j] == str2[i]:
                    print("{0} is the same as {1}".format(str1[j], str2[i]))
                    dp[j + 1][i + 1] = dp[j][i] + 1
                else:
                    dp[j + 1][i + 1] = maX
        return dp[-1][-1]

    def printMatrix(self, matrix):
        col = len(matrix[0])
        row = len(matrix)
        for i in range(row):
            for j in range(col):
                print (matrix[i][j]),
            print("\t")
    def printStrMatrix(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        for j in range(len2 + 1):
            if j == 0:
                print(0),
            else:
                print(str2[j - 1]),
            for i in  range(len1):
                if j == 0:
                    print(str1[i] + " "),
                else:
                    print(str1[i] + str2[j - 1]),
            print("\t")
        print(str1 + str2)

str1 = "bedaacbade"
str2 = "dccaeedbeb"
print(Solution().LCS(str1,str2))
