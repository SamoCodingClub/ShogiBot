"""IMPORTANT: notation idea: xy(piece)(spacer), ex. 12p/43k/."""
"""why do we have main.py in github are we even using it"""
import math
import tkinter as tk
import time
from shogi_game.py import *

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


# setup for classes
board = Board([], "", 0)
p1 = Player([])
p2 = Player([])

# setup with functions
board.set(
    "00L/10N/20S/30G/40K/50G/60S/70N/80L/11B/71R/02P/12P/22P/32P/42P/52P/62P/72P/82P/08l/18n/28s/38g/48k/58g/68s/78n/88l/17b/77r/06p/16p/26p/36p/46p/56p/66p/76p/86p"
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
    board.movePiece(input_arr)
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
