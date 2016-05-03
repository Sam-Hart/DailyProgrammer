class driver:
	gossips = []

	def __init__(self):
		self.gossips.append(gossip())

class gossip:
	pass

d = driver()
print(len(driver.gossips))