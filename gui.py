from tkinter import *
from tkinter import scrolledtext
import keyboard
import tkinter as tk
import threading
import nltk
import sys
import os
from WordPredictor import WordPredictor

class GUI:

    def __init__(self):
        self.curText = ''
        self.shouldReplace = False
        self.lenReplace = 0
        self.root = Tk()
        self.root.title('Word Predictor')
        self.root.geometry('400x300')
        self.textBox = scrolledtext.ScrolledText(self.root, width=49, height=5, wrap   = 'word')
        self.listBox = Listbox(self.root,width=49, height=5)
        self.listBox.bind("<Double-Button-1>", self.clickedList)
        self.textBox.grid(column = 1, row = 0)
        self.listBox.grid(column = 1, row = 2)

    def bindCallback(self, callback):
        self.callback = callback

    def clickedList(self, event):
        if self.shouldReplace ==False:
            self.insertWord(self.listBox.get(ACTIVE))
        else:
            self.replaceWord(self.listBox.get(ACTIVE))
        self.clearList()
        self.callback()

    def getText(self):
        self.curText = self.textBox.get('1.0',tk.END)
        return self.curText

    def setList(self, guesses):
        self.clearList()
        for i in range(len(guesses)):
            if guesses[i] != None:
                self.listBox.insert(i, guesses[i])
            else:
                self.listBox.insert(i,'')

    def insertWord(self, word):
        self.textBox.insert(tk.END, word + ' ')

    def replaceWord(self,word):
        self.textBox.insert(tk.END,word + ' ')

    def clearList(self):
        self.listBox.delete(0,END)


def main():
    wp = WordPredictor()
    wp.process_file('corpus.txt')
    gui = GUI()
    operating_thread = threading.Thread(target = run_process)
    keyboardThread.start()
    gui.root.mainloop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
