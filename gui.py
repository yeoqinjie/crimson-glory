import tkinter as tk

window = tk.Tk()

v = tk.IntVar()
cb1_checked = tk.BooleanVar()
cb2_checked = tk.BooleanVar()

label = tk.Label(text="Choose your course", justify=tk.LEFT).pack()

# rb1 = tk.Radiobutton(text="Python", variable=v, value=1).pack(anchor=tk.W)
# rb2 = tk.Radiobutton(text="C++", variable=v, value=2).pack(anchor=tk.W)

cb1 = tk.Checkbutton(text="Python", variable=cb1_checked).pack(anchor=tk.W)
cb2 = tk.Checkbutton(text="C++", variable=cb2_checked).pack(anchor=tk.W)

# label2 = tk.Label(text="Select Radio", justify=tk.LEFT, textvariable=v).pack()

window.mainloop()
