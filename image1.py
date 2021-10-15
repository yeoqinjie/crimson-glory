import tkinter as tk

window = tk.Tk()
window.title('Window Title')

canvas = tk.Canvas(width=300, height=300)
canvas.pack()

img = tk.PhotoImage(file="house_1.ppm")
canvas.create_image(20, 20, anchor=tk.NW, image=img)

tk.mainloop()