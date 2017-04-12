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

def get_adjacent(graph, vertix):
	adj = []
	for i in range(len(graph[vertex])):
		if graph[vertix][i] != 0:
			adj.append(i)
	return adj

def dijkstra(graph, source):
	"Apply the Dijkstra algorithm"

	vertices = []
	Q = PriorityQueue()
	way = []

	for v in range(len(graph)):
		vertices.append(Vertex())
		Q.add_with_priority(v, vertices[v].dist)

	vertices[source] = Vertex(dist=0)
	Q.decrease_priority(source, 0)

	print(Q)

	while len(Q) != 0:
		u = Q.extract_min()
		way.append(u)
		for neighbor in get_adjacent(graph, u[1]):
			alt = graph[u[1]][neighbor] + u.dist
			print('a')
			if (type(vetices[neighnor].dist) == str) or (int(vertices[neighborn].dist) > alt):
				print('b')
				vertices[neighbor].dist = alt
				vertices[neighbor].prev = u
				Q.decrease_priority(neighbor, alt)

	return [v.dist for v in vertices]




graph = build_graph(8)
print_graph(graph)
w = dijkstra(graph, 5)
print(w)
