"""
IMPORTANT. PLEASE READ
The file was not directly put from getting_games into here. It was cleaned using manual find and replace. This process was fast enough (about 30 seconds) to be deemed unnecessary to right code for. Just so you know. 

hands are not being stored, so I guess you can choose the format in which to store them. I suggest something like (position)/(position)\(thing in hand)\(thing in hand)/-1 or something I really dont know


array of games, which are arrays of moves and winner at the end i guess
whatever you want
this can be done without board but then I wouldn't be able to copy and paste code

this is also really inefficient because I used board

please someone redo this but actually good (actually not that important because it worked fast enough on a 1500 line dataset)
"""

"""
outputs one game per line in a text file, with the winner at the end, ex. (position)/(position)/(position)/-1

generates one game per move to maximize value of the dataset
"""

class Board: #KEEP SEPERATE FROM SHOGI_GAME BOARD THEY ARE DIFFERENT SO DO NOT TRY AND IMPORT ALSO IDK WHY IT IS TAKING IN CONSTANTS SO I GOT RID OF THAT PART AND WE PROBABLY SHOULD DO THAT FOR OTHER BOARD. oops my caps lock was on.
	def __init__(self, array, string):
		self.array = array
		self.string = string
		self.num_turn = 0
		self.p1 = []
		self.p2 = []
	def set(self, string): #does not load hands
			self.array = [["." for y in range(9)] for x in range(9)]
			input_arr = string.split("/")
			for entry in input_arr:
				try:
					self.array[int(entry[0])][int(entry[1])] = entry[2]
				except:
					print("There was an error with setting the board. The issue was with:", entry)
	
	def createSet(self): #does not save hands
			entry = 1
			set_str = ""
			for y in range(9):
				for x in range(9):
					if self.array[x][y] != ".":
						if entry > 1:
							set_str += "/"
						set_str += str(x) + str(y) + str(self.array[x][y])
						entry +=1
			return set_str
	
	def movePiece(self, x1, y1, x2, y2):
		if self.array[x2][y2] != ".":
			if self.num_turn %2 == 0:
				self.p1.append(self.array[x2][y2].upper())

			else:
				try:
					self.p2.append(self.array[x2][y2].upper())
				except:
					print(self.array)
		
		self.array[x2][y2] = self.array[x1][y1]
		self.array[x1][y1] = "."
	def placePiece(self, x, y, piece):
		self.array[x][y] = piece
	
	def promotePiece(self, piece):
		if self.num_turn % 2 == 0:
			if piece == "P" or piece == "L" or piece == "S" or piece == "N" or  piece == "P":
				return "g"
			elif piece == "B":
				return "h"
			elif piece == "R":
				return "d"
		else:
			if piece == "P" or piece == "L" or piece == "S" or piece == "N" or  piece == "P":
				return "G"
			elif piece == "B":
				return "H"
			elif piece == "R":
				return "D"

def reencode(src, dst):
	pieces = ["p", "n", "l", "g", "k", "s", "r", "b", "h", "d"]
	letter_num = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8}
	temp_array = []
	
	#turn input file into array that can be used
	with open(src, "r") as inputfp, open(dst, 'w') as outputfp:
		for line in inputfp:
			inp = line[:-1]
			temp_array.append(inp.split(", "))
		#turn array into text that sets up a board, add to file
		g = 0
		for game in temp_array:
			board = Board([], "")
			
			fthem = False
			asq = 0
			board.set("00L/10N/20S/30G/40K/50G/60S/70N/80L/11B/71R/02P/12P/22P/32P/42P/52P/62P/72P/82P/08l/18n/28s/38g/48k/58g/68s/78n/88l/17b/77r/06p/16p/26p/36p/46p/56p/66p/76p/86p")
			for move in game:
				asq+=1
				#print(board.array)
				try:
					print(board.array)
					if fthem and "}" in move:
						fthem = False
					elif fthem:
						continue
					if "{" in move:
						fthem = True
					if move[-1] == "+":
						print(board.promotePiece(move[0]))
						board.placePiece(abs(int(move[1]) - 9), letter_num[move[2]], board.promotePiece(move[0]))
						print(board.array)
						print("ak")
						board.movePiece(abs(int(move[1]) - 9), letter_num[move[2]], abs(int(move[4]) - 9), letter_num[move[5]])
						board.num_turn += 1
					elif move[0].lower() in pieces:
						print(asq)
						board.movePiece(abs(int(move[1]) - 9), letter_num[move[2]], abs(int(move[4]) - 9), letter_num[move[5]])
						board.num_turn += 1
					elif move[1] == "*": #they use proper notation for 
						if board.num_turn %2 == 0:
							board.p1.pop(board.p1.index(move[0]))
						else:
							board.p1.pop(board.p1.index(move[0]))
						if board.num_turn % 2 == 0:
							board.placePiece(abs(int(move[1]) - 9),letter_num[move[2]], letter_num(move[0]).lower())
						else:
							board.placePiece(abs(int(move[1]) - 9),letter_num[move[2]], letter_num(move[0]).upper())
						board.num_turn+=1
					new_board = board.createSet()
					outputfp.write(new_board)
					outputfp.write("/")
					outputfp.write("^")
					count = 0
					for entry in board.p1:
						if type(entry) != type("lkjdsfjdsafds"):
							continue
						if count == 0:
							outputfp.write("!")
							count += 1
						outputfp.write(entry)
						outputfp.write("/")asd 
					if count ==1:		
						outputfp.write("&")
					count = 0
					for entry in board.p2:
						if type(entry) != type("lkjdsfjdsafds"):
							continue
						if count == 0:
							outputfp.write("?")
							count += 1
						outputfp.write(entry)
						outputfp.write("/")
					if count == 1:
						outputfp.write("@")
					outputfp.write("/")
					outputfp.write(game[-1][:-1])
					outputfp.write("\n")
				except:
					print("error", move)
			g += 1
	print("Reencode Complete")
	

reencode('./database.txt', './games_I_think') #put files here please. here
