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
			return True
 
class Pawn(Piece):
	def genMoves(self):
		moves = []
		new_y = self.y + self.color
		if self.checkBounds(self.x, new_y) and board.array[self.x][new_y] == ".":
			moves.append([self.x, new_y])
		return moves
	

class King(Piece):
	def genMoves(self):
		moves = []
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (delta_x != 0 and delta_y != 0) and self.checkBounds(new_x, new_y) and board.array[new_x][new_y] == ".":
					moves.append([new_x, new_y])
		return moves

class Knight(Piece):
	def genMoves(self):
		moves = []
		if board.array[self.x + 1][self.y + (2*self.color)] == "." :
			moves.append([self.x + 1],[self.y +(2*self.color)])
		if board.array[self.x - 1][self.y + (2*self.color)] == ".":
			moves.append([self.x - 1],[self.y +(2 *self.color)])
		return moves

class Bishop(Piece):
	def genMoves(self):
		moves = []
		l = [-1,1]
		for t in l:
			for s in l:
				if t == -1 and l == -1:
					break
				c =board.array[self.x + t][self.y + l]
				count = 1
				while c == ".":
					moves.append([self.x + (count * t), self.y + (count * l)])
					count += 1
					c = board.array[self.x + (count * t)][self.y + (count * l)]
		return moves

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

class Lance(Piece):

	def genMoves(self):
		moves = []
		c = board.array[self.x][self.y+self.color]
		print([self.x,self.y])
		count = 1
		while c == ".":
			moves.append([self.x,self.y + (count*self.color)])
			count += 1
			c = board.array[self.x][self.y + (count*self.color)]
			print(count)
		return moves
			
			
class Rook(Piece):
	def genMoves(self):
		moves = []
		c = [self.x, self.y]
		l = [-1, 1]
		for x in l:
			count = 1
			if self.checkBounds(self.x, self.y + (count*x)):
				c = board.array[self.x][self.y+(count*x)]
			while self.checkBounds(self.x, self.y + (x*count)):
					c = board.array[self.x][self.y + (count*x)]
					if c == ".":
						moves.append([self.x,self.y + (x*count)])
						count += 1
					else:
						break
			count = 1
			if self.checkBounds(self.x+(count*x), self.y):
				c = board.array[self.x+(count*x)][self.y]
			while self.checkBounds(self.x+(count*x),self.y):
				c = board.array[self.x+(count*x)][self.y]
				if c == ".":
					moves.append([self.x + (x*count),self.y])
					count += 1
				else:
					break
		return moves

class Gold_General(Piece): #can abreviate if you want
	def genMoves(self):
		moves = []
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (delta_x == 0 and delta_y == -1) and delta_y != 0 and self.checkBounds(new_x, new_y) and board.array[new_x][new_y] == ".":
					moves.append([new_x, new_y])
		return moves

#I'm not doing promoted pieces

class Board:
	def __init__(self, array, string, p1_hand, p2_hand, set_str):
		self.array = array
		self.p1_hand = p1_hand
		self.p2_hand = p2_hand
	
	def setup(self):
		self.array = [["." for y in range(9)] for x in range(9)]
		#innermost ranks in setup
		for x in range(9):
			self.array[x][6] = Pawn( -1, x, 6)
			self.array[x][2] = Pawn( 1, x, 2)
		#I'm not making this efficient
		#middle ranks in setup
		"""self.array[1][1] = Bishop("b", 0)
		self.array[1][7] = Bishop("B", 1)
		
		self.array[7][1] = Rook("r", 0)
		self.array[7][7] = Rook("R", 1)
		#outermost ranks in setup
		self.array[0][0] = Lance("l", 0)
		self.array[1][0] = Knight("n", 0)
		self.array[2][0] = Silver_General("s", 0)
		self.array[3][0] = Gold_General("g", 0)
		self.array[4][0] = King("k", 0)
		self.array[5][0] = Gold_General("g", 0)
		self.array[6][0] = Silver_General("s", 0)
		self.array[7][0] = Knight("n", 0)
		self.array[8][0] = Lance("l", 0)
		
		self.array[0][8] = Lance("L", 1)
		self.array[1][8] = Knight("K", 1)
		self.array[2][8] = Silver_General("S", 1)
		self.array[3][8] = Gold_General("G", 1)
		self.array[4][8] = King("K", 1)
		self.array[5][8] = Gold_General("G", 1)
		self.array[6][8] = Silver_General("S", 1)
		self.array[7][8] = Knight("N", 1)
		self.array[8][8] = Lance("L", 1)"""
	#char_to_class = {
	def set(self):
		input_arr = self.set_str.split("/")
		for entry in input_arr:
			try:
				self.array[int(entry[0])][int(entry[1])] = entry[2]
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
						self.string += str(self.array[x][y].__class__.__name__)[0] + " "
					else:
						self.string += str(self.array[x][y].__class__.__name__)[0].lower() + " "
		self.string += "\n"
		print(self.string)

board = Board([], "", [], [], "")

board.setup()
board.print()
l = Rook(-1, 2,3)
print(l.genMoves())