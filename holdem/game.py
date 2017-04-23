import os
from player import player
from agent import agent
from agentai import agentai
class game():
	players=[]
	def _init_(self):
		self.players=[]
# Selects types of Players playing the Game
	def selectPlayers(self,dealerObj):
		print("******************************************")
		print(" Welcome to the Texas Hold'em Poker Game")
		print("******************************************")
		print("What Game would you like :")
		print("1. Human PLayer vs  Human Player")
		print("2. AI Agent     vs  Human Player")
		print("3. AI Agent     vs  AI Agent")
		selected= 0
		while(selected == 0):
			choice=int(input("Enter Your Choice : "))
			if (choice ==1):
				self.players.append(player(1, dealerObj))
				self.players.append(player(2, dealerObj))
				selected= 1
				return self.players
			elif (choice==2):
				level=int(input("Enter Agent Level (1-5) :"))
				level1=self.checkLevel(level)
				if (level1==5):
					self.players.append(agentai(1, dealerObj))
				else:
					self.players.append(agent(1, dealerObj,level1))
				self.players.append(player(2, dealerObj))
				selected= 1
				return self.players
			elif(choice==3):
				level=int(input("Enter Agent 1 Level (1-5) :"))
				level1=self.checkLevel(level)
				if level1==5:
					self.players.append(agentai(1, dealerObj))
				else:
					self.players.append(agent(1, dealerObj,level1))
				level=int(input("Enter Agent 2 Level (1-5) :"))
				level2=self.checkLevel(level)
				if level2==5:
					self.players.append(agentai(2, dealerObj))
				else:
					self.players.append(agent(2, dealerObj,level1))
				selected= 1
				return self.players
			else:
				print("You Entered the Wrong choice")
#Checks If the Agent Level entered is in range	
	def checkLevel(self,level):
		while(level>5):
			level=int(input("Level Out of Range, Please Enter Again (1-5) :"))
		return level
			
