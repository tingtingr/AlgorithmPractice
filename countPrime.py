class Solution(object):
	def countPrime(self, n):
	    def isPrime(n):
            if n % x in [2,3,5,7,9,11] == 0:
                return True
            else:
                return False
        return isPrime(9)