class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def __init__(self, r):
		self.root = r

	def constructMaximumBinaryTree(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if len(nums) == 0:
			return None

		if len(nums) == 1 and self.root is None:
			return TreeNode(nums[0])
		
		root_val = max(nums)
		middle = nums.index(root_val)

		root = TreeNode(root_val)
		root.left = self.constructMaximumBinaryTree(nums[:middle])
		root.right = self.constructMaximumBinaryTree(nums[middle+1:])
		return root


n = [3,2,1,6,0,5]
root = None
tree = Solution(root)
print(tree.constructMaximumBinaryTree(n).val)