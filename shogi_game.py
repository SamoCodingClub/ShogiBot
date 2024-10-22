"""IMPORTANT: notation idea: xy(piece)(spacer), ex. 12p/43k/."""
"""why do we have main.py in github are we even using it"""
import math
import tkinter as tk
import time

root = tk.Tk()

boardSize = 20
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

for num in range(0, 10):
    canvas.create_line(boardSize * num,
                       0,
                       boardSize * num,
                       9 * boardSize,
                       tags="lines")
    canvas.create_line(0,
                       boardSize * num,
                       9 * boardSize,
                       boardSize * num,
                       tags="lines")


class Player:

    def __init__(self, hand):
        self.hand = hand


# get input here? can have target coordinates in the class or in a function i dunno


# IMPORTANT the x and y doesn't work right now fix it later
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

class Empty:
	def __init__(self):
		self.color = 0
		self.__class__.__name__ = " "

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
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.__class__.__name__ = "N"  #should this be a thing
	def genMoves(self):
		moves = []
		if board.array[self.x + 1][self.y + (2 * self.color)].color != self.color :
			moves.append([self.x + 1,self.y +(2 * self.color)])
		if board.array[self.x - 1][self.y + (2 * self.color)].color != self.color:
			moves.append([self.x - 1,self.y + (2 * self.color)])
		return moves
	def promote(self):
		board.array[self.x][self.y] = Gold_General(self.color, self.x, self.y,)

class Bishop(Piece): #this is bad and all the stuff like it is bad and I am sorry for that add checkBounds so that it actually does something
	def genMoves(self):
		moves = []
		l = [-1, 1]
		for t in l:
			for s in l:
				if t == -1 and s == -1:
					break
				temp = board.array[self.x + t][self.y + s]
				count = 1
				while self.checkBounds(self.x + (count*t), self.y + (count*s)) and temp.color != self.color:
					moves.append([self.x + (count * t), self.y + (count * s)])
					temp = board.array[self.x + (count * t)][self.y + (count * s)]
					count += 1
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
		while self.checkBounds(self.x,self.y+(count*self.color)) and temp.color != self.color:
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



# might be broken
"""class Dragon_Horse(Piece): #this doesnt work either
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
    return moves"""


class Board:  # must incrememnt turn_num after each move please please

    def __init__(self, array, string, turn_num):
        self.array = array
        self.string = string
        self.turn_num = turn_num

    def set(self, string):  # does not load hands
        self.array = [[Empty() for y in range(9)] for x in range(9)]
        input_arr = string.split("/")
        for entry in input_arr:
            try:
                if entry.islower():
                    color = -1
                else:
                    color = 1
                entry = entry.lower()
                if "p" in entry:  # change to switch if you want to switch later maybe possibly
                    self.array[int(entry[0])][int(entry[1])] = Pawn(
                        color, int(entry[0]), int(entry[1]))
                elif "k" in entry:
                    self.array[int(entry[0])][int(entry[1])] = King(
                        color, int(entry[0]), int(entry[1]))
                elif "s" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Silver_General(
                        color, int(entry[0]), int(entry[1]))
                elif "r" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Rook(
                        color, int(entry[0]), int(entry[1]))
                elif "b" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Bishop(
                        color, int(entry[0]), int(entry[1]))
                elif "g" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Gold_General(
                        color, int(entry[0]), int(entry[1]))
                elif "n" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Knight(
                        color, int(entry[0]), int(entry[1]))
                elif "l" in entry:
                    self.array[int(entry[0])][int(entry[1])] = Lance(
                        color, int(entry[0]), int(entry[1]))
            except:
                print(
                    "There was an error with setting the board. The issue was with:",
                    entry)

    def print(self):
        self.string = ""
        for y in range(9):
            self.string += "\n"
            for x in range(9):
                if self.array[x][y] == " ":
                    self.string += self.array[x][y] + " "
                else:
                    if self.array[x][y].color == 1:
                        self.string += str(
                            self.array[x][y].__class__.__name__)[0] + " "
                    else:
                        self.string += str(self.array[x][y].__class__.__name__
                                           )[0].lower() + " "
        self.string += "\n"
        print(self.string)

    def createSet(self):  # does not save hands
        entry = 1
        set_str = ""
        for y in range(9):
            for x in range(9):
                print(self.array[x][y])
                if self.array[x][y].__class__.__name__ != " ":
                    if entry > 1:
                        set_str += "/"
                    set_str += str(self.array[x][y].x) + str(
                        self.array[x][y].y)
                    if self.array[x][y].color == -1:
                        set_str += self.array[x][y].__class__.__name__[
                            0].lower()
                    else:
                        set_str += self.array[x][y].__class__.__name__[0]
                    entry += 1
        return set_str

    def checkLegality(self, target_x, target_y, new_x,
                      new_y):  # says returns new but where is new
        original = self.createSet()
        board.movePiece([[target_x, target_y], [new_x, new_y]])
        for y in range(9):
            for x in range(9):
                if self.turn_num % 2 == 0 and self.array[x][
                        y].__class__.__name__ == "King" and self.array[x][
                            y].color == -1:
                    king_pos = [x, y]
                elif self.turn_num % 2 == 1 and self.array[x][
                        y].__class__.__name__ == "King" and self.array[x][
                            y].color == 1:
                    king_pos = [x, y]
        for y in range(9):
            for x in range(9):
                if self.array[x][y].__class__.__name__ != " ":
                    for entry in self.array[x][y].genMoves():
                        if entry == king_pos:
                            self.set(original)
                            self.turn_num-=1

    def movePiece(
        self, input_arr
    ):  # temp, remember to change both their x and y position in the array and their x and y position in the class
        print(input_arr)
        l = self.array[input_arr[0][0]][input_arr[0][1]].genMoves()
        if [input_arr[1][0], input_arr[1][1]] in l: # this is sort of bad on both of our parts but I will fix it later. 
            for entry in l:
                if entry == [input_arr[1][0], input_arr[1][1]]:
                    if self.array[input_arr[1][0]][input_arr[1][1]].color == -1:
                        p1.hand.append(self.array[input_arr[1][0]][input_arr[1][1]])
                    elif self.array[input_arr[1][0]][input_arr[1][1]].color == 1:
                        p2.hand.append(self.array[input_arr[1][0]][input_arr[1][1]])
                    self.array[input_arr[1][0]][input_arr[1][1]] = self.array[
                        input_arr[0][0]][input_arr[0][1]]  # moves piece
                    self.array[input_arr[1][0]][input_arr[1][1]].x = input_arr[1][
                        0]  # sets new x
                    self.array[input_arr[1][0]][input_arr[1][1]].y = input_arr[1][
                        1]  # sets new y
                    self.array[input_arr[0][0]][
                        input_arr[0][1]] = Empty()  # sets old position to empty
                    self.turn_num += 1

        else:
            print("Illegal move, please try again.")
            # get input again

    def placePiece(self, piece, x, y):  # im confused reading this
        hand = []
        if self.turn_num % 2 == 1:
            hand = p2.hand
        elif self.turn_num % 2 == 0:
            hand = p1.hand
        boolean_value = False
        for p in hand:
            if p.__class__.__name__ == piece.__class__.__name:
                boolean_value = True
        if boolean_value and self.array[x][
                y].__class__.__name__ == " ":  # this eats your piece if you place it wrong fix later
            self.array[x][y] = piece
            if len(self.array[x][y].genMoves()) == 0:
                self.array[x][y] = Empty()
                return False
            for z in range(9):
                if self.array[x][z].__class__.__name__ == "Pawn":
                    self.array[x][y] = Empty()
                    return False
        return True


# setup for classes
board = Board([], "", 0)
p1 = Player([])
p2 = Player([])

# setup with functions
board.set(
    "00L/10N/20S/30G/40K/50G/60S/70N/80L/11B/71R/02P/12P/22P/32P/42P/52P/62P/72P/82P/08l/18n/28s/38g/48k/58g/68s/78n/88l/77b/17r/06p/16p/26p/36p/46p/56p/66p/76p/86p"
)


def draw_piece(x, y, p):
    if p.color == 1:
            canvas.create_text(boardSize * (x + .5),
                   boardSize * (8.5 - y),
                   text=p.__class__.__name__[0],
                   font=("Ariel", 15),
                   fill="black",
                   tags=f"p{x}{y}")
    else:
        canvas.create_text(boardSize * (x + .5),
               boardSize * (8.5 - y),
               text=str.lower(p.__class__.__name__[0]),
               font=("Ariel", 15),
               fill="black",
               tags=f"p{x}{y}")



def draw_board():
    for x, column in enumerate(board.array):
        for y, thing in enumerate(column):
            draw_piece(x, y, board.array[x][y])


def a_literal_move(input_str):
    x1 = int(input_str[0])
    y1 = int(input_str[1])
    x2 = int(input_str[2])
    y2 = int(input_str[3])
    input_arr = [[x1, y1], [x2, y2]]
    board.checkLegality(x1,y1,x2,y2)
    canvas.delete(f"p{x1}{y1}")
    canvas.delete(f"p{x2}{y2}")
    draw_piece(x1, y1, board.array[x1][y1])
    draw_piece(x2, y2, board.array[x2][y2])


x=-1
y=-1

def click_pos(event):
    global x, y
    x = math.floor((event.x + .5) / boardSize)
    y = math.floor(9 - (event.y  / boardSize))

draw_board()
root.update()
run = True
thing = ""
root.bind(f"<Button-1>", click_pos)
t = 0
name = ""
while run is True:
    if board.turn_num % 2 == 0:
        name = "ONE"
        time = 1
    elif board.turn_num % 2 == 1:
        name = "TWO"
        time = -1
    canvas.delete("moveText")
    canvas.create_text(boardSize * 9 + 80,
           boardSize * (4.5),
           text=f"PLAYER {name}'S\n      MOVE",
           font=("Ariel", 12),
           fill="black",
           tags="moveText")
    root.update()
    if x != -1 and y != -1:

        t += 1
        if t % 2 == 1:
            if board.array[x][y].color == time:
                thing = f"{x}{y}"
                print(thing)
            else:
                t = 0
            x, y = -1, -1
        else:
            a_literal_move(f"{thing}{x}{y}")
            print(f"{x}{y}")
            board.print()
            t = 0


root.mainloop()
