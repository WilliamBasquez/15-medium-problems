def pruneTree(root):
	if root == None:
		return None

	if root.left is None:
		#go right subtree
	else:
		if root.left == 0:
			if root.left != 1:
				root.left = None
			else
				#go to the right
		else:
			#go left
			