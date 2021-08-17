import tkinter as tk

window = tk.Tk()

# sets the window size to 500px x 300px
window.geometry("500x300")
window.title('Window Title')

v = tk.IntVar()
# create a new radio button
radio = tk.Radiobutton(text='Label', variable=v, value=1)

# put the radio button into the window
radio.pack()

window.mainloop()
