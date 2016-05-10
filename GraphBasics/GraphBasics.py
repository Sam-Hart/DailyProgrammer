class Node():
	def __init__(self, value):
		self.__id = value
		self.__neighbors = []

	def createEdge(self, node):
		if node not in self.__neighbors:
			self.__neighbors.append(node)

	def id(self):
		return self.__id

	def neighbors(self):
		return self.__neighbors

class simulate():
	def __init__(self, inputFile):
		self.__inputFile = open(inputFile, 'r')
		self.__nodes = []
		self.__graph = []

		fileLines = []

		for line in self.__inputFile:
			line = line.rstrip('\n')
			fileLines.append(line)

		for val in range(1, int(fileLines[0]) + 1):
			newNode = Node(val)
			self.__nodes.append(newNode)

		self.__graph = [[0 for x in range(int(fileLines[0]))] for y in range(int(fileLines[0]))]


		for line in fileLines[1:]:
			line = line.rstrip('\n')
			nodes = line.split(" ")
			nodeA = self.__nodes[int(nodes[0]) - 1]
			nodeB = self.__nodes[int(nodes[1]) - 1]
			self.__graph[nodeA.id() - 1][nodeB.id() - 1] = 1
			self.__graph[nodeB.id() - 1][nodeA.id() - 1] = 1

			nodeA.createEdge(nodeB)
			nodeB.createEdge(nodeA)


		for node in self.__graph:
			print(node)

		for node in self.__nodes:
			print("Node {0} has a degree of {1}".format(node.id(), len(node.neighbors())))



graphSimulate = simulate("ExampleInput.txt")

graphSimulate = simulate("ChallengeInput.txt")