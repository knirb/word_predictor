from tkinter import *

from tkinter import scrolledtext
import tkinter as tk
root = Tk()
root.title('Word predictor')
root.geometry('400x300')
textBox = scrolledtext.ScrolledText(root, width=49, height=5, wrap   = 'word')
listBox = Listbox(root,width=49, height=5)
textBox.insert(tk.INSERT, "testing")
print(textBox.get("wordstart", tk.END))
textBox.grid(column = 1, row = 0)
listBox.grid(column = 1, row = 2)
root.mainloop()
