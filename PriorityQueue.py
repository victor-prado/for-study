from Vertex import Vertex

class PriorityQueue(list):

	def __init__(self):
		list.__init__(self) #Another way to write that would be: super().__init__()


	def add_with_priority(self, vertex, priority):
		"Add a vertex (or node) with its priority in the queue"
		self.append(Vertex(vertex, priority))


	def decrease_priority(self, vertex, priority):
		"Decrease the vertex's priority to the new 'priority' value"

		for i in range(len(self)):
			if self[i].num == vertex:
				self[i] = Vertex(vertex, priority)


	def extract_min(self):
		"Extract and returns the minimum value in the queue"
		
		value = self[0]
		for v in self:
			if value.greater_than(v):
				value = v

		self.remove(value)
		return value
