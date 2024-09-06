"""IMPORTANT: notation idea: xy?(spacer), ex. 12p/43k/."""
"""ISSUE: both knights and kings are k when printed. 
Might not matter though because this isn't the true board that we are going to use, henry can deal with it"""

class Piece:
	def __init__(self, name, color, x, y): #-1 is black, 1 is white
		self.name = name
		self.color = color
		self.x = x
		self.y = y
	
	def checkBounds(x, y):
		if x < 0 or x > 9 or x < 0 or y > 9:
			return False
		else:
			return True
 
class Pawn(Piece):
	def genMoves():
		moves = []
		new_y = self.y + self.color
		if self.checkBounds(self.x, new_y) and board.array[self.x][new_y] == ".":
			moves.append([self.x, new_y])
		return moves
	

class King(Piece):
	def genMoves():
		moves = []
		for delta_x in range(-1, 2):
			for delta_y in range(-1, 2):
				new_x = self.x + self.color * delta_x
				new_y = self.y + self.color * delta_y
				if (x != 0 and y != 0) and self.checkBounds(new_x, new_y) and board.array[new_x][new_y] == ".":
					moves.append([new_x, new_y])
		return moves

class Knight(Piece):
	def genMoves():
		moves = []
		if board.array[self.x + 1][self.y +2] == ".":
			moves.append([self.x + 1],[self.y +2])
		if board.array[self.x - 1][self.y +2] == ".":
			moves.append([self.x - 1],[self.y +2])
		return moves

class Bishop(Piece):
	def genMoves():
		moves = []
		for t in l:
			a = t
			for s in l:
				b = s
				if a == -1 and b == -1:
					break
				c =board.array[self.x + a][self.y + b]
				count = 1
				while c == ".":
					moves.append([self.x + (count * a), self.y + (count * b)])
					count += 1
					c = board.array[self.x + (count * a)][self.y + (count * b)]
		return moves

class Silver_General(Piece): #can abreviate if you want
	pass

class Lance(Piece):
	def genMoves():
		moves = []
		c = board.array[self.x][self.y+1]
		count = 1
		while c == ".":
			moves.append([self.x],[self.y + count])
			count += 1
			c = board.array[self.x][self.y + count]
		return moves
			
			
class Rook(Piece):
	pass

class Gold_General(Piece): #can abreviate if you want
	pass

#I'm not doing promoted pieces

class Board:
	def __init__(self, array, string, p1_hand, p2_hand, set_str):
		self.array = array
		self.p1_hand = p1_hand
		self.p2_hand = p2_hand
	
	def setup(self): """delete this when set is done"""
		self.array = [["." for y in range(9)] for x in range(9)]
		#innermost ranks in setup
		for x in range(9):
			self.array[x][6] = Pawn("P", -1, x, 6)
			self.array[x][2] = Pawn("p", 1, x, 2)
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
	
	def print(self): """ISSUE: both knights and kings are k because of how this works"""
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
#this is almost as long as my minesweeper already
