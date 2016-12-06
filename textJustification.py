import sys
import math
class Solution(object):
    def fullJustify(self, words, maxWidth):
        dp = [[0 for i in range(len(words))] for j in range(len(words))]
      	self.printM(dp)
      	for i in range(len(words)):
      		for j in range(i,len(words)):
      			if i == j:
      				dp[i][j] = (maxWidth - len(words[i]))**2
      			else:
      				pre = dp[i][j-1]
      				cur = len(words[j]) + 1
      				if pre != "INF" and math.sqrt(pre) - cur > 0:
      					dp[i][j] = pre + cur**2 - 2*cur*int(math.sqrt(pre))
      					
      	self.printM(dp)
    def printM(self, m):
    	for i in range(len(m)):
    		for j in range(len(m[0])):

    			print("%3s" % (m[i][j],)),
    		print("\b")
    	print("\n")
    # 	# calculate the square difference, from words[i] to words[j],including j, for maxWidth
    # def calSum(self, maxWidth, words, i, j):
    # 	sumV = len(words[i])
    # 	for x in range(i + 1, j + 1):
    # 		sumV += len(words[x]) + 1
    # 	if maxWidth >= sumV:
    # 		return (maxWidth- sumV)**2
    # 	else:
    # 		return "INF"
s= "Wenting is a cute baby pig".split()
length = 10
Solution().fullJustify(s,length)
# Wenting is
# a cute 
# baby progressing

# greedy will be to fill the line as much as possible if doesn't fit then move it to the next line
# how ever, it would be bad if the end line only has one character. the sum of square would be greater than
# dp Solution

# # for dp solution, it is like calculating longest valid parentheses. we will compare each length. 
# from 0:2, not including 2
# 0:1, 1:2, 2:3, 3:4,... length 1
# 0:2,1:3,3:5,4:6.... length 2

# so let's calculate.


# i in s  	0, 1, 2, 3, 4, 5, 
# length		7, 2, 1, 4, 4, 3
# L - len(s[i]) ** 2, [0, -1]
# length(1)   9, 64, 81, 36, 36, 49
# L - len(s[i] + s[i+1] + 1) [0, -2]
# length(2)   0, 36, 16,  1, 4
# L - len(s[i] + s[i + 1] + s[i + 2] + 2)
# length(3)   INF, 1, INF, INF
# L- len(s[i], s[i + 1], s[i + 2], s[i + 3])
# lengthg(4)  INF, INF, INF


# # so the matrix looks like(write it up)



# Note, Once, S[i][length] == INF, stop progressing

