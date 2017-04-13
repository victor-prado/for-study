import random
from PriorityQueue import PriorityQueue
from Vertex import Vertex


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

def get_adjacent(graph, source):
	adj = []
	for i in range(len(graph[source])):
		if graph[source][i] != 0:
			adj.append(i)
	return adj

def dijkstra(graph, source):
	'''Apply the Dijkstra algorithm and return the a list where
	each position represents a vertice and its content represents 
	the predecessor'''

	vertices = [] #list of vertices
	Q = PriorityQueue() #priority queue

	#fills 'vertices' and 'Q', each vertex receive the distance iquals infinity
	for v in range(len(graph)):
		vertices.append(Vertex(v)) 
		Q.add_with_priority(v, vertices[v].dist)

	#the source vertex receive the distance zero
	vertices[source] = Vertex(num=source, dist=0)
	Q.decrease_priority(source, 0)

	while len(Q) != 0:
		u = Q.extract_min()

		for neighbor in get_adjacent(graph, u.num):
			alt = graph[u.num][neighbor] + u.dist
			Alt = Vertex(neighbor, alt)

			if vertices[neighbor].greater_than(Alt):
				vertices[neighbor].dist = alt
				vertices[neighbor].prev = u.num
				Q.decrease_priority(neighbor, alt)

	return [v.prev for v in vertices]



