from tkinter import *
import keyboard
from tkinter import scrolledtext
import tkinter as tk
import threading
import nltk

curText = ''
root = Tk()
root.title('Word predictor')
root.geometry('400x300')
textBox = scrolledtext.ScrolledText(root, width=49, height=5, wrap   = 'word')
listBox = Listbox(root,width=49, height=5)
textBox.insert(tk.INSERT, "testing if this is \n working ")
print(textBox.get('1.0', tk.END))
textBox.grid(column = 1, row = 0)
listBox.grid(column = 1, row = 2)

def keyCheck():
    while True:
        try:
            #TODO: tokenizecurtext - > compare to ngrams -> show suggestions in listbox
            waitForKey()

            print('You Pressed A Key!')
        except:
            break
def waitForKey():
    key = keyboard.read_key()
    keyboard.on_release_key(key,getText,suppress= True)
def getText(e):
    try:
        curText = textBox.get('1.0',tk.END)
    except:
        print('something went wrong')
def tokenizeText(): #TODO: write this function
    pass
def compare
def main():
    keyboardThread = threading.Thread(target = keyCheck)
    keyboardThread.start()
    root.mainloop()
    keyboardThread.join()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
