from tkinter import *
from tkinter import scrolledtext
import keyboard
import tkinter as tk
import threading
import nltk
import sys
import os
from TrigramModel import TrigramModel
from WordPredictor import WordPredictor

# curText = ''
# root = Tk()
# root.title('Word predictor')
# root.geometry('400x300')
# textBox = scrolledtext.ScrolledText(root, width=49, height=5, wrap   = 'word')
# listBox = Listbox(root,width=49, height=5)
# textBox.insert(tk.INSERT, "testing if this is \n working ")
# print(textBox.get('1.0', tk.END))
# textBox.grid(column = 1, row = 0)
# listBox.grid(column = 1, row = 2)
class GUI:
    def __init__(self):
        self.curText = ''
        self.root = Tk()
        self.root.title('Word Predictor')
        self.root.geometry('400x300')
        self.textBox = scrolledtext.ScrolledText(self.root, width=49, height=5, wrap   = 'word')
        self.listBox = Listbox(self.root,width=49, height=5)
        self.textBox.insert(tk.INSERT, "This is our example text this is ")
        self.textBox.grid(column = 1, row = 0)
        self.listBox.grid(column = 1, row = 2)
    def getText(self):
        self.curText = self.textBox.get('1.0',tk.END)
        return self.curText
    def setList(self, guesses): #TODO figure out listbox
        for guess in guesses:
            self.listBox.insert(END, guess)
    def tokenize(self, text_in): #TODO: write this function
        try :
            tokens = nltk.word_tokenize(text_in)
            return tokens
        except LookupError :
            nltk.download('punkt')
            tokens = nltk.word_tokenize(text_in)
            return tokens
    def run_loop(self):
        self.root.mainloop()

    # def keyCheck():
    #     while True:
    #         try:
    #             #TODO: tokenizecurtext - > compare to ngrams -> show suggestions in listbox
    #             waitForKey()
    #             tokens = tokenize(curText)
    #             print(curText)
    #             #suggestions = findSuggestions(tokens[len(tokens)-4:len(tokens)-1])
    #             print('You Pressed A Key!')
    #         except:
    #             break
    # def waitForKey():
    #     key = keyboard.read_key()
    #     keyboard.on_release_key(key,doNothing,suppress= True)
    # def getText(e):
    #     try:
    #         curText = textBox.get('1.0',tk.END)
    #     except:
    #         print('something went wrong')
def run_process():
    pass

def main():
    wp = WordPredictor()
    wp.process_file('corpus.txt')
    gui = GUI()
    operating_thread = threading.Thread(target = run_process)
    keyboardThread.start()
    gui.root.mainloop()
    # keyboardThread.join()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
