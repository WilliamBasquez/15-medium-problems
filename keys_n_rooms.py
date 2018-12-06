class dsf:
	def __init__(self, n):
		self.forest = [-1] * n

	def find(self, a):
		if not 0 <= a <= len(self.forest):
			return -1

		if self.forest[a] < 0:
			return a

		self.forest[a] = self.find(self.forest[a])

		return self.forest[a]

	def union(self, a, b):
		ra = self.find(a)
		rb = self.find(b)

		if ra != rb:
			self.forest[rb] = ra

def canVisitAllRooms(nums):
	f = dsf(len(num))
	for room in rooms:
		f.union(room,rooms[room])

	root = 0
	for i in f.forest:
		if i < 0:
			root+=1

	if root > 1:
		return False