"""IMPORTANT: notation idea: xy?(spacer), ex. 12p/43k/."""
"""ISSUE: both knights and kings are k when printed. 
Might not matter though because this isn't the true board that we are going to use, henry can deal with it"""

class Piece:
	def __init__(self, color, x, y): #-1 is black, 1 is white
		self.color = color
		self.x = x
		self.y = y
	
	def checkBounds(self, x, y):
		if x < 0 or x > 8 or y < 0 or y > 8:
			return False
		else:
			return Trueyyyyy

class Empty:
	def __init__(self):
		self.color = 0
		self.__class__.__name__ = "."

class Pawn(Piece):
	def genMoves(self):
		moves = []
		new_y = self.y + self.color
		if self.checkBounds(self.x, new_y) and board.array[self.x][new_y].color != self.color:
			moves.append([self.x, new_y])
		return moves
	
	def promote(self):
		board.array[self.x][self.y] = Gold_General(self.color, self.x, self.y,)
	

class King(Piece):
	def genMoves(self):
		moves = []
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (delta_x != 0 and delta_y != 0) and self.checkBounds(new_x, new_y) and board.array[new_x][new_y].color != self.color:
					moves.append([new_x, new_y])
		return moves

class Knight(Piece):
	def genMoves(self):
		moves = []
		if board.array[self.x + 1][self.y + (2 * self.color)].color != self.color :
			moves.append([self.x + 1],[self.y +(2 * self.color)])
		if board.array[self.x - 1][self.y + (2 * self.color)].color != self.color:
			moves.append([self.x - 1],[self.y + (2 * self.color)])
		return moves
	def promote(self):
		board.array[self.x][self.y] = Gold_General(self.color, self.x, self.y,)

class Bishop(Piece): #this is bad and all the stuff like it is bad and I am sorry for that add checkBounds so that it actually does something
	def genMoves(self):
		moves = []
		l = [-1,1]
		for t in l:
			for s in l:
				if t == -1 and l == -1:
					break
				temp = board.array[self.x + t][self.y + l]
				count = 1
				while self.checkBounds(temp[0], temp[1]) and temp.color != self.color:
					moves.append([self.x + (count * t), self.y + (count * l)])
					count += 1
					temp = [self.x + (count * t),self.y + (count * l)]
		return moves
		
	def promote(self):
		board.array[self.x][self.y] = Dragon_Horse(self.color, self.x, self.y)

class Silver_General(Piece): #can abreviate if you want
	def genMoves(self):
		moves = []
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (delta_x == 0 and delta_y == -1) and delta_y != 0 and self.checkBounds(new_x, new_y) and board.array[new_x][new_y] == ".":
					moves.append([new_x, new_y])
		return moves
	
	def promote(self):
		board.array[self.x][self.y] = Gold_General(self.color, self.x, self.y,)

class Lance(Piece):
	def genMoves(self):
		moves = []
		temp = board.array[self.x][self.y+self.color]
		print([self.x,self.y])
		count = 1
		while self.checkBounds(temp) and temp.color != self.color:
			moves.append([self.x,self.y + (count*self.color)])
			count += 1     
			temp = board.array[self.x][self.y + (count*self.color)]
			print(count)
		return moves
		
	def promote(self): 
		board.array[self.x][self.y] = Gold_General(self.color, self.x, self.y,)
			
			 
class Rook(Piece):
	def genMoves(self):
		moves = []
		temp = [self.x, self.y]
		l = [-1, 1]
		for x in l:
			count = 1
			if self.checkBounds(self.x, self.y + (count*x)):
				temp = board.array[self.x][self.y+(count*x)]
			while self.checkBounds(self.x, self.y + (x*count)):
					temp = board.array[self.x][self.y + (count*x)]
					if temp.color != self.color:
						moves.append([self.x,self.y + (x*count)])
						count += 1
					else:
						break
			count = 1
			if self.checkBounds(self.x+(count*x), self.y):
				temp = board.array[self.x+(count*x)][self.y]
			while self.checkBounds(self.x+(count*x),self.y):
				temp = board.array[self.x+(count*x)][self.y]
				if temp.color != self.color:
					moves.append([self.x + (x*count),self.y])
					count += 1
				else:
					break
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (delta_x != 0 and delta_y != 0) and self.checkBounds(new_x, new_y) and board.array[new_x][new_y].color != self.color and [new_x,new_y] not in moves:
					moves.append([new_x, new_y])
		return moves
		
		def promote(self):
			board.array[self.x][self.y] = Dragon_King(self.color, self.x, self.y)

class Gold_General(Piece): #can abreviate if you want
	def genMoves(self):
		moves = []
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (delta_x == 0 and delta_y == -1) and delta_y != 0 and self.checkBounds(new_x, new_y) and board.array[new_x][new_y]!= self.color:
					moves.append([new_x, new_y])
		return moves

class Dragon_Horse(Piece): #this doesnt work either
	def genMoves(self):
		moves = []
		l = [-1,1]
		for t in l:
			for s in l:
				if t == -1 and l == -1:
					break
				temp = board.array[self.x + t][self.y + l]
				count = 1
				while self.checkBounds(temp[0], temp[1]) and temp.color != self.color:
					moves.append([self.x + (count * t), self.y + (count * l)])
					count += 1
					temp = [self.x + (count * t),self.y + (count * l)]
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (delta_x != 0 and delta_y != 0) and self.checkBounds(new_x, new_y) and board.array[new_x][new_y].color != self.color and [new_x,new_y] not in moves:
					moves.append([new_x, new_y])
		return moves
class Dragon_King(Piece):
	def genMoves(self):
		moves = []
		temp = [self.x, self.y]
		l = [-1, 1]
		for x in l:
			count = 1
			if self.checkBounds(self.x, self.y + (count*x)):
				temp = board.array[self.x][self.y+(count*x)]
			while self.checkBounds(self.x, self.y + (x*count)):
					temp = board.array[self.x][self.y + (count*x)]
					if temp.color != self.color:
						moves.append([self.x,self.y + (x*count)])
						count += 1
					else:
						break
			count = 1
			if self.checkBounds(self.x+(count*x), self.y):
				temp = board.array[self.x+(count*x)][self.y]
			while self.checkBounds(self.x+(count*x),self.y):
				temp = board.array[self.x+(count*x)][self.y]
				if temp.color != self.color:
					moves.append([self.x + (x*count),self.y])
					count += 1
				else:
					break
		return moves
#I'm not doing promoted pieces

class Board:
	def __init__(self, array, string, p1_hand, p2_hand):
		self.array = array
		self.string = string
		self.p1_hand = p1_hand
		self.p2_hand = p2_hand
	
	def set(self, string):
		self.array = [[Empty() for y in range(9)] for x in range(9)]
		input_arr = string.split("/")
		for entry in input_arr:
			try:
				if entry.islower():
					color = -1
				else:
					color = 1
				entry = entry.lower()
				if "p" in entry: #change to switch if you want to switch later maybe possibly
					self.array[int(entry[0])][int(entry[1])] = Pawn(color, int(entry[0]), int(entry[1]))
				elif "k" in entry:
					self.array[int(entry[0])][int(entry[1])] = King(color, int(entry[0]), int(entry[1]))
				elif "s" in entry:
					self.array[int(entry[0])][int(entry[1])] = Silver_General(color, int(entry[0]), int(entry[1]))
				elif "r" in entry:
					self.array[int(entry[0])][int(entry[1])] = Rook(color, int(entry[0]), int(entry[1]))
				elif "b" in entry:
					self.array[int(entry[0])][int(entry[1])] = Bishop(color, int(entry[0]), int(entry[1]))
				elif "g" in entry:
					self.array[int(entry[0])][int(entry[1])] = Gold_General(color, int(entry[0]), int(entry[1]))
				elif "n" in entry:
					self.array[int(entry[0])][int(entry[1])] = Knight(color, int(entry[0]), int(entry[1]))
				elif "l" in entry:
					self.array[int(entry[0])][int(entry[1])] = Lance(color, int(entry[0]), int(entry[1]))
			except:
				print("There was an error with setting the board. The issue was with:", entry)
	
	def print(self):
		self.string = ""
		for y in range(9):
			self.string += "\n"
			for x in range(9):
				if self.array[x][y] == ".":
					self.string += self.array[x][y] + " "
				else:
					if self.array[x][y].color == 1:
						self.string += self.array[x][y].__class__.__name__[0] + " "
					else:
						self.string += self.array[x][y].__class__.__name__[0].lower() + " "
		self.string += "\n"
		print(self.string)
	  
	def createSet(self): #there is no way I did this well it looks so bad
		entry = 1
		set_str = ""
		for y in range(9):
			for x in range(9):
				if self.array[x][y] != ".":
					if entry > 1:
						set_str += "/"
					set_str += str(self.array[x][y].x) + str(self.array[x][y].y)
					if self.array[x][y].__class__.__name__ == "Knight": #this probably could be done better
						if self.array[x][y].color == -1:
							set_str += "n"
						else:
							set_str += "N"
					else:
						if self.array[x][y].color == -1:
							set_str += self.array[x][y].__class__.__name__[0].lower()
						else:
							set_str += self.array[x][y].__class__.__name__[0]
					entry +=1
		return set_str
	
	def checkLegality(self, target_x, target_y, new_x, new_y): #checks current board position, not future like it is supposed to
		possible_moves = []
		for y in range(9):
			for x in range(9):
				if self.array[x][y].__class__.__name__ != ".":
					for entry in self.array[x][y].genMoves():
						possible_moves.append(entry)
		for entry in possible_moves:
			if 
				
	
	def movePiece(self): #temp
		input_str = input("xyxy because I'm lazy\n") #as this is just a test I'll assume they did the correct format
		input_arr = [[int(input_str[0]), int(input_str[1])], [int(input_str[2]), int(input_str[3])]]
		print(input_arr)
		for entry in self.array[input_arr[0][0]][input_arr[0][1]].genMoves():
			if entry == input_arr[1]:
				if self.array[input_arr[1][0]][input_arr[1][1]] != "." and self.array[input_arr[1][0]][input_arr[1][1]].color == -1:
					self.p2_hand.append(self.array[input_arr[1][0]][input_arr[1][1]])
				elif self.array[input_arr[1][0]][input_arr[1][1]] != ".":
					self.p1_hand.append(self.array[input_arr[1][0]][input_arr[1][1]])
				self.array[input_arr[1][0]][input_arr[1][1]] = self.array[input_arr[0][0]][input_arr[0][1]]
				self.array[input_arr[0][0]][input_arr[0][1]] = "."
		

board = Board([], "", [], [])

board.set("00L/10N/20S/30G/40K/50G/60S/70N/80L/11B/71R/02P/12P/22P/32P/42P/52P/62P/72P/82P/08l/18n/28s/38g/48k/58g/68s/78n/88l/17b/77r/06p/16p/26p/36p/46p/56p/66p/76p/86p")
board.print()
board.movePiece()
board.print()
print(board.createSet())