import os
# This class Maintains a record of the winners of all games played in a batch 
class winner():
	pl=[]
	pt=[]
	hand=[]
	maximum=0
	def _init_(self):
		self.pl=[]
		self.pt=[]
		self.hand=[]
		self.maximum=0
# Finds hand name based on the numbers 
	# 9 Royal flush
        # 8 Straight flush
        # 7 Four of a Kind
        # 6 Full house
        # 5 Flush
        # 4 Straight
        # 3 Three of a kind
        # 2 Two pair
        # 1 Pair
        # 0 Nothing
	def findHand(self,h):
		if(h==0):
			return'Nothing'
		elif(h==1):
			return 'Pair'
		elif (h==2):
			return 'Two pair'
		elif (h==3):
			return "Three of a kind"
		elif (h==4):
			return "Straight"
		elif (h==5):
			return "Flush"
		elif (h==6):
			return "Full House"
		elif (h==7):
			return "Four of a Kind"
		elif (h==8):
			return "Straight flush"
		elif (h==9):
			return "Royal flush"

	def findMax(self,h):
		if(self.maximum<h):
			self.maximum=h
		

	def add(self,name,point,h):
		self.pl.append(name)
		self.pt.append(point)
		self.findMax(h)
		self.hand.append(self.findHand(h))
		
		return
       
		
# Prints game statistics on the Screen	
	def printStats(self):
		p1win=0
		p2win=0
		p1won=0
		p2won=0
		print("=========================================================")
		print("| Winning Player | Points Added |    Hand \t\t|")
		print("=========================================================")
		for i in range(len(self.pt)):
			print("|\t"+str(self.pl[i])+"\t |  \t"+str(self.pt[i])+"\t|  "+str(self.hand[i])+" \t\t| ")
			if(self.pl[i]==1):
				p1win+=1
				p1won+=self.pt[i]
			elif(self.pl[i]==2):
				p2win+=1
				p2won+=self.pt[i]
			else:
				p1win+=1
				p2win+=1
				p1won+=self.pt[i]
				p2won+=self.pt[i]
				
		print("=========================================================")
		print("\nBest Hand : ",self.findHand(self.maximum))
		print("Player 1 Won : "+str(p1win)+ " games and $ "+str(p1won))
		print("Player 2 Won : "+str(p2win)+ " games and $ "+str(p2won))
		print("\n********************************************************\n")

		return
	
#logs game statistics to a File	
	def log(self):
		file = open("gameLog.txt","w")
		file.truncate(0);
		p1win=0
		p2win=0
		p1won=0
		p2won=0
		file.write("=========================================================")
		file.write("\n| Winning Player | Points Added |    Hand \t\t|")
		file.write("\n=========================================================")
		for i in range(len(self.pt)):
			file.write("\n|\t"+str(self.pl[i])+"\t |  \t"+str(self.pt[i])+"\t|  "+str(self.hand[i])+" \t\t| ")
			if(self.pl[i]==1):
				p1win+=1
				p1won+=self.pt[i]

			elif(self.pl[i]==2):
				p2win+=1
				p2won+=self.pt[i]
			else:
				p1win+=1
				p2win+=1
				p1won+=self.pt[i]
				p2won+=self.pt[i]
				
		file.write("\n=========================================================")
		file.write("\n\nBest Hand : "+str(self.findHand(self.maximum)))
		file.write("\nPlayer 1 Won : "+str(p1win)+ " games and $ "+str(p1won))
		file.write("\nPlayer 2 Won : "+str(p2win)+ " games and $ "+str(p2won))
		file.write("\n\n********************************************************\n")
		file.close();

		return
	
