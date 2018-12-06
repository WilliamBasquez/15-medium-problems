import math
def topKFrequent(nums, k):
	if k >= len(nums):
		return nums

	dic = {}
	ans = []
	min_n = math.inf * -1
	for n in nums:
		if n in dic:
			dic[n] += 1
		else:
			dic[n] = 1

def main():
	numbers = [1,1,1,2,2,3,3,3,3,2,2,2]
	n = 2
	print(topKFrequent(numbers, n))

main()