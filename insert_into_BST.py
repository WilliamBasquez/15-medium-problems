class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def __init__(self):
		self.root = None

	def insertIntoBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		"""
		node = TreeNode(val)

		if self.root is None:
			self.root = node
		else:
			if root.val < node.val:
				if root.right is None:
					root.right = node
				else:
					self.insertIntoBST(root.right, node.val)
			else:
				if root.left is None:
					root.left = node
				else:
					self.insertIntoBST(root.left, node.val)