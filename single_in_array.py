def singleNonDuplicate(nums):
	left = 0
	right = 1

	if len(nums) < 2:
		return 0

	for i in range(len(nums)-1):
		if nums[left] != nums[right]:
			return nums[left]
		left+=2
		right+=2

