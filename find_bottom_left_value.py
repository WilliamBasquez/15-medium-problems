"""
d = height of the tree
"""
def findBottomLeftValue(root, d):
	if d == 0 and root.left is None:
		return root

	if root.left in not None:
		return findBottomLeftValue(root.left, d-1)
	else:
		return findBottomLeftValue(root.right, d-1)
