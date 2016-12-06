class Solution(object):
    def combine(self, n, k):
    	res = []
    	if n <= 0 or k <= 0 or k < n:
    		return res
        # nums = [i + 1 for i in range(n)]

        self.helper(n,k,res,[],1)
        return res
    def helper(self, n, k, res, sub, index):
        if k == 0:
            res.append(sub)
            return
        for i in range(index, n + 1):
        	sub.append(n)
            # if len(sub) < k:
            self.helper(n, k - 1, res, sub, i + 1)
            del sub[-1]