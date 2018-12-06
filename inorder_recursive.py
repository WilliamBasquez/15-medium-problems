def inOrder(root, l):
	if root:
		inOrder(root.left)
		l.append(root.val)
		inOrder(root.right)
	return l