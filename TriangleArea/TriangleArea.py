class Triangle():
	def __init__(self, vertices):
		self.__vertices = list(zip(*[iter(vertices)]*2))
	
	def calcSide(self, vert1, vert2):
		return (((vert2[0] - vert1[0])**2) + ((vert2[1] - vert1[1])**2))**.5

	def getSideLengths(self):
		vert1 = self.__vertices[0]
		vert2 = self.__vertices[1]
		vert3 = self.__vertices[2]

		return [self.calcSide(vert1, vert2), self.calcSide(vert1, vert3), self.calcSide(vert2, vert3)]
		
	def getArea(self):
		sides = self.getSideLengths()
		semPerim = (sides[0] + sides[1] + sides[2]) / 2

		return (semPerim*(semPerim - sides[0])*(semPerim - sides[1])*(semPerim - sides[2]))**.5



triangleData = "1 3 9 5 6 0"
triangle = Triangle([int(coord) for coord in triangleData.split(" ")])
print(triangle.getArea())
