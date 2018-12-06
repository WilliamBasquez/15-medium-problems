#Assuming we know the height of the tree

def printTree(root):
	columns = root.if_full()
	tree = [""] * columns
	for i in range(root.height):
		tree.append([""] * root.height)

	l = 0
	r = columns

	for i in range(root.height):
		middle = (l+r)//2
		for i in range(columns):
			tree[middle] = root.item
		if root.left != None:
			r = middle-1
		else:
			l = middle+1
