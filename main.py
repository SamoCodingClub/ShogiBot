import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
for num in range(0, 10):
  canvas.create_line(20 + 20 * num, 20, 20 + 20 * num, 200)
  canvas.create_line(20, 20 + 20 * num, 200, 20 + 20 * num)



root.mainloop()
