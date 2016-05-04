class driver:
	_stop = 0

	def assignRoute(self, route):
		if not isinstance(route, list):
			raise TypeError("Route must be a list")
		self._route = route


	def currentStop(self):
		return self._route[self._stop]

	def move(self):
		self._stop += 1
		if self._stop >= len(self._route):
			self._stop = 0
		
	


	def produceRoute(self):
		return self._route


class simulate:
	
	def __init__(self, inputFile):
		self._inputFile = open(inputFile, 'r')
		self._drivers = []
		
		for line in self._inputFile:
			line = line.rstrip('\n')	
			self._drivers.append(driver())
			self._drivers[-1].assignRoute(line.split(" "))
		
		for counter in range(0, 481):
			for d in self._drivers:
				
				d.move()



			

		




simulate("ExampleInput1.txt")