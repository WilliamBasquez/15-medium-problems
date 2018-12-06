import math
"""
I looked for an iterative inOrder function and used it to keep the parameters from the given function
"""
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BST_Sum:
	def __init__(self, r):
		self.root = r

	def rangeSumBST(self, root, L, R):
		"""
		:type root: TreeNode
		:type L: int
		:type R: int
		:rtype: int
		"""
		answer = []
		temp = root

		Stack = []
		nodes_visited = 0
		while not nodes_visited:
			if temp is not None:
				Stack.append(temp)
				temp = temp.left
			else:
				if len(Stack) > 0:
					temp = Stack.pop()
					if temp.val <= R and temp.val >= L:
						answer.append(temp.val)
					temp = temp.right
				else:
					nodes_visited = 1
		return sum(answer)

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.right = TreeNode(15)
root.left.right = TreeNode(7)
root.right.left = None
root.right.right = TreeNode(18)

tree = BST_Sum(root)
print(tree.rangeSumBST(tree.root, 7, 15))