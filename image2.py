import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
canvas = tk.Canvas(width=300, height=300)
canvas.pack()

img = ImageTk.PhotoImage(Image.open('house_1.jpg'))
canvas.create_image(20, 20, anchor=tk.NW, image=img)

tk.mainloop()