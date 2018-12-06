def findDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	l = []
	dic = {}
	for each in nums:
		if each not in dic:
			dic[each] = 1
		else:
			dic[each] +=1

	for item in dic:
		if dic[item] == 2:
			l.append(item)

	return l

def main():
	print("hi")
	listl = [4,3,2,7,8,2,3,1]
	print(findDuplicates(listl))

main()