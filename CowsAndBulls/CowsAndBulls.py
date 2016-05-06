from random import randint
import math
class game():
	
	def __init__(self):
		self.__player = player()
		self.__number = self.generateNumber()

	
	def generateNumber(self):
		return randint(1, 9999)

	def play(self):
		print("Welcome to Cows and Bulls!\n")
		
		while not int(self.__player.sayGuess()) == self.__number:
			guessNumber = int(self.__player.guess())
			
			bulls = 0
			cows = 0

			comparisonNumber = self.__number
			comparisonList = []
			guessList = []
			while comparisonNumber > 0:
				comparisonRemainder = comparisonNumber % 10
				comparisonNumber = math.floor(comparisonNumber / 10)
				comparisonList.append(comparisonRemainder)
				
				guessRemainder = guessNumber % 10
				guessNumber = math.floor(guessNumber / 10)
				guessList.append(guessRemainder)

				if guessRemainder == comparisonRemainder:
					guessList.remove(guessRemainder)
					comparisonList.remove(comparisonRemainder)
					cows += 1
			bulls = len(list(set(guessList).intersection(comparisonList)))

			print("Cows: ", cows, "\n")	
			print("Bulls: ", bulls, "\n")


		print("Congratulations!\n")
		print("The number was {0}!".format(self.__number))

class player():
	def __init__(self):
		self.__name = input("Please enter a name:\n")
		self.__guess = 0

	def sayGuess(self):
		return self.__guess

	def guess(self):
		self.__guess = input("Please enter a number:\n")
		return self.__guess
	

def main():
	cbGame = game()
	cbGame.play()



if __name__ == '__main__':
	main()