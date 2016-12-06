# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.



class Solution(object):
    def candy(self, ratings):
        dp = [1 for i in range(len(ratings) + 1)]

        for i in range(len(ratings)):
        	val = ratings[i]
