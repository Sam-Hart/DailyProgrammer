from time import sleep
from functools import reduce
from operator import or_
class driver:
	
	def __init__(self):
		self._stop = 0
		self._gossips = []
		self._gossips.append(gossip())
		self._telling = False
		self._listening = False

	def assignRoute(self, route):
		if not isinstance(route, list):
			raise TypeError("Route must be a list")
		self._route = route


	def currentStop(self):
		return self._route[self._stop]

	def move(self):
		if not(self._telling or self._listening):
			self._stop = (self._stop + 1) % len(self._route)
		self._telling = False
		self._listening = False
		
	def produceRoute(self):
		return self._route

	def tellGossip(self):
		return self._gossips

	def isTelling(self):
		self._telling = True


	def listenToGossip(self, gossips):
		if len(gossips) > 0:
			self._listening = True
			for g in gossips:
				self._gossips.append(g)


class gossip:
	def __init__(self):
		self._content = "A gossip"

class simulate:
	
	def __init__(self, inputFile):
		self._inputFile = open(inputFile, 'r')
		self._drivers = []
		self._allGossipsTransferred = False
		self._allGossipsTransferredTime = 0
		
		for line in self._inputFile:
			line = line.rstrip('\n')
			#Create new driver for each line
			self._drivers.append(driver())
			
			self._drivers[-1].assignRoute(line.split(" "))


		all_stops = reduce(or_, (set(driver.produceRoute()) for driver in self._drivers), set())
		all_gossip = reduce(or_, (set(driver.tellGossip()) for driver in self._drivers), set())
		
		#Main loop to process all interactions between drivers
		for counter in range(0, 480):

			#Find each potential stop point for each iteration
			#and assign a list to it
			currentStops = {stop: [] for stop in all_stops}

			for d in self._drivers:
				currentStops[d.currentStop()].append(d)
				
			for stop, drivers in currentStops.items():
				for listeningDriver in drivers:
					otherDrivers = [d for d in drivers if d is not listeningDriver]
					for o in otherDrivers:
						missingGossips = [g for g in o.tellGossip() if g not in listeningDriver.tellGossip()]
						if len(missingGossips) > 0:
							o.isTelling()

						listeningDriver.listenToGossip(missingGossips)


			for d in self._drivers:
				d.move()

				
			if all(set(d.tellGossip()) == set(all_gossip) for d in self._drivers) and not self._allGossipsTransferred:
			 	self._allGossipsTransferred = True
			 	self._allGossipsTransferredTime = counter

	
	def simulationStatus(self):
		return (self._allGossipsTransferred, self._allGossipsTransferredTime)

		

ExampleInput1 = simulate("ExampleInput1.txt")
print(ExampleInput1.simulationStatus())

ExampleInput2 = simulate("ExampleInput2.txt")
print(ExampleInput2.simulationStatus())

ChallengeInput1 = simulate("ChallengeInput1.txt")
print(ChallengeInput1.simulationStatus())

ChallengeInput2 = simulate("ChallengeInput2.txt")
print(ChallengeInput2.simulationStatus())