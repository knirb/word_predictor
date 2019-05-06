from tkinter import *
from tkinter import scrolledtext
root = Tk()
root.title('Word predictor')
root.geometry('400x300')
textBox = scrolledtext.ScrolledText(root, width=49, height=5)
textBox.grid(column = 1, row = 0)
root.mainloop()
