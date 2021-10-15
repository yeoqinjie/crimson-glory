import tkinter as tk

window = tk.Tk()

# sets the window size to 500px x 300px
window.geometry("500x300")
window.title('Window Title')

v = tk.IntVar()
# create a new radio button
label = tk.Label(text="Gender")

# v = 1 is male, v = 2  is female
radio = tk.Radiobutton(text='Male', variable=v, value=1)
radio2 = tk.Radiobutton(text='Female', variable=v, value=2)

# put the radio button into the window
label.pack()
radio.pack()
radio2.pack()

window.mainloop()
