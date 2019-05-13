from tkinter import *
from tkinter import scrolledtext
import keyboard
import tkinter as tk
import threading
import nltk
import sys
import os
from TrigramModel import TrigramModel

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
            tokens = tokenize(curText)
            print(curText)
            print(tokens[len(tokens)-4:len(tokens)-1])
            suggestions = findSuggestions(tokens[len(tokens)-4:len(tokens)-1])
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
def tokenize(text_in): #TODO: write this function
    try :
        tokens = nltk.word_tokenize(text_in)
        return tokens
    except LookupError :
        nltk.download('punkt')
        tokens = nltk.word_tokenize(text_in)
        return tokens

def main():
    trigram_model = TrigramModel()
    trigram_model.process_files('corpus.txt')
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
