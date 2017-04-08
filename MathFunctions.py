import random

def lcm(numbers):
	"Return the least commom multiple of numbers's elements"

	i = 2
	length = len(numbers)
	lcm = 1
	while (sum(numbers) != len(numbers)):
		usefull = False
		for j in range(length):
			if (numbers[j]%i == 0):
				numbers[j] = numbers[j]/i
				usefull=True

		if (usefull):
			lcm*=i
		else:
			i+=1

	return lcm

def gcf(numbers):
	"Return the greatest commom factor of numbers's elements"

	i, gcf = 2, 1
	length = len(numbers)
	while (sum(numbers) != len(numbers)):
		usefull = False
		k = 0
		for j in range(length):
			if (numbers[j]%i == 0):
				numbers[j] = numbers[j]/i
				usefull = True
				k+=1

		if (not usefull):
			i+=1
		if (k == length):
			gcf*=i

	return gcf

def build_graph(nodes_number, maw=1, oriented=False):
	'''Returns a random graph with 'nodes_number' nodes, represented by a adjacency matrix
	maw: max arc weight'''

	graph = [[0 for j in range(nodes_number)] for i in range(nodes_number)]

	if oriented:
		for i in range(nodes_number):
			for j in range(nodes_number):
				a = random.randint(0, maw)
				graph[i][j] = a
			graph[i][i] = 0
		return graph	

	else:
		for i in range(nodes_number):
			for j in range(i, nodes_number):
				a = random.randint(0, maw)
				graph[i][j] = a
				graph[j][i] = a

			graph[i][i] = 0

		return graph

def print_graph(simple_graph):
	"Print a simple graph represented by a adjacency matrix"
	num = 1
	for n in simple_graph:
		print(str(num) + ' ' + str(n))
		num += 1


class Node():
	'''Node of a graph. Weight is a number, 
	state can be anything, but could be usefull like a string'''

	def __init__(self, weight=1, state=None):
		self.weight = weight


class Arc():
	"Arc of a graph. Tail and head are nodes"

	def __init__(self, tail, head, weight=1):
		self.tail = tail
		self.head = head
		self.weight = weight



class Simple_Graph():

	def __init__(self, nodes, arcs):
		self.nodes = nodes
		self.arcs = arcs




