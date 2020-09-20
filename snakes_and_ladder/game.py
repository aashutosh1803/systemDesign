import random
import time
from collections import defaultdict
from constants import *
from colorama import Fore


class Snake:

	def __init__(self):
		self.snakes = SNAKES

	def getSnakes(self):
		return self.snakes


class Ladder:

	def __init__(self):
		self.ladders = LADDERS

	def getLadder(self):
		return self.ladders


class Dice:

	def getDiceNumber(self):
		# playerInput = 0
		# while not (1 <= playerInput <=6):
		# 	playerInput = int(input('Enter a number between 1 to 6: '))
		#
		# dice = playerInput
		return random.randint(1, 6)


class Board:

	def __init__(self):
		self.startPosition = BOARD_START_POS
		self.endPosition = BOARD_END_POS
		self.snakes = Snake().getSnakes()
		self.ladders = Ladder().getLadder()
		self.playerPieces = defaultdict(lambda: 0)

		if not self.isBoardValid():
			raise Exception("Sorry, Board is not valid")

	def isBoardValid(self):
		for snake in self.snakes:
			if not (self.startPosition <= snake <= self.endPosition and self.startPosition <= self.snakes[snake] <= self.endPosition):
				return False
		for ladder in self.ladders:
			if not (self.startPosition <= ladder <= self.endPosition and self.startPosition <= self.ladders[ladder] <= self.endPosition):
				return False
		return True

	def updatePlayerPieces(self, playerId, playerPosition, reason):
		if reason == PLAYER_MOVE_DICE_REASON:
			if self.playerPieces[playerId] + playerPosition <= BOARD_END_POS:
				self.playerPieces[playerId] += playerPosition
		else:
			self.playerPieces[playerId] = playerPosition

	def getPlayerCurrentPosition(self, playerId):
		return self.playerPieces[playerId]

	def relevantSnake(self, position):
		if position in self.snakes:
			return self.snakes[position]
		return None

	def relevantLadder(self, position):
		if position in self.ladders:
			return self.ladders[position]
		return None


class Player:
	playerId = 1

	def __init__(self):
		self.id = Player.playerId
		Player.playerId += 1
		self.position = BOARD_START_POS

	def getPlayerId(self):
		return self.id


class GameService:

	def startGame(self, board, players, dice):
		gameOn = True
		print(Fore.RESET + "Game is On")
		while gameOn:
			for player in players:
				playerId = player.getPlayerId()
				playerPos = board.getPlayerCurrentPosition(playerId)
				print(Fore.RESET + "********* Player {} is playing *********".format(playerId))
				print(Fore.RESET + "Currently on number {} in Board".format(playerPos))

				time.sleep(3)
				diceNum = dice.getDiceNumber()
				print(Fore.RESET + "Dice Rolling and Number on Dice is .... {}".format(diceNum))

				time.sleep(3)
				board.updatePlayerPieces(playerId, diceNum, PLAYER_MOVE_DICE_REASON)
				print(Fore.RESET + "Moved to number {}".format(board.getPlayerCurrentPosition(playerId)))

				if board.relevantSnake(board.getPlayerCurrentPosition(playerId)):
					time.sleep(3)
					board.updatePlayerPieces(playerId, board.relevantSnake(board.getPlayerCurrentPosition(playerId)), PLAYER_MOVE_SNAKE_REASON)
					print(Fore.RED + "Snake Present...  and dropped player to number {}".format(board.getPlayerCurrentPosition(playerId)))

				if board.relevantLadder(board.getPlayerCurrentPosition(playerId)):
					time.sleep(3)
					board.updatePlayerPieces(playerId, board.relevantLadder(board.getPlayerCurrentPosition(playerId)), PLAYER_MOVE_LADDER_REASON)
					print(Fore.GREEN + "Ladder Present...  and lifted player to number {}".format(board.getPlayerCurrentPosition(playerId)))

				if self.isWinner(board.getPlayerCurrentPosition(playerId)):
					time.sleep(3)
					print(Fore.RESET + "********* Player {}'s turn end *********".format(playerId))
					print(Fore.RESET + "Game Over".format(playerId))
					gameOn = False
					break

				print(Fore.RESET + "********* Player {}'s turn end *********".format(playerId))
			if not gameOn:
				break

	def isWinner(self, playerPosition):
		return playerPosition == BOARD_END_POS


def game():
	players = [Player() for i in range(0, NUMBER_OF_PLAYERS)]
	board = Board()
	dice = Dice()
	gameService = GameService()
	gameService.startGame(board, players, dice)


if __name__ == "__main__":
	game()