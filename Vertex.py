class Vertex():

	def __init__(self, num, dist="infinity", prev=None):
		self.num = num
		self.dist = dist
		self.prev = prev

	def greater_than(self, vertex):

		if self.dist == "infinity":
			return True

		elif vertex.dist == "infinity":
			return False

		elif self.dist > vertex.dist:
			return True

		return False