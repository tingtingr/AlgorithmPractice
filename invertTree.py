class Solution(object):
	def invertTree(self, root):
		if root:
			root.left = root.right
			self.invertTree(root.left)
			self.invertTree(root.right)
		return root	

