from WordPredictor import WordPredictor
from gui import GUI
import threading
import keyboard
import time
import sys
import os

gui = GUI()
word_predictor = WordPredictor()

def update():
    try:
        time.sleep(0.01)
        user_input = gui.getText()
        user_input = user_input[:-1]
        user_word_list = user_input.split()
        print('DOING NEW UPDATE')
        print('user_input[-1]: '+ user_input)
        if user_input[-1] == ' ':
            gui.shouldReplace = False
        else:
            gui.shouldReplace = True
            gui.lenReplace = len(user_word_list[-1])

        guess_1,guess_2,guess_3 = None,None,None

        # guess next full word using past 2 words
        if user_input[-1] == " " and len(user_word_list) >= 2:
            guess_1, guess_2, guess_3 = word_predictor.guess_next_word_trigram(user_word_list[-2], user_word_list[-1])

        # guess next full word using previous word
        if (user_input[-1] == " " and len(user_word_list) == 1) or ( guess_1==None and guess_2==None and guess_3==None ):
            guess_1, guess_2, guess_3 = word_predictor.guess_next_word_bigram(user_word_list[-1])


        # if next word predictor still has no guesses after trigram and bigram model
        if(user_input[-1] == " ") and (guess_1==None and guess_2==None and guess_3==None):
            guess_1, guess_2, guess_3 = word_predictor.guess_next_word_unigram()

        # guess ending of current word
        if (user_input[-1] != " "):
            guess_1, guess_2, guess_3 = word_predictor.finish_word(user_word_list[-1].lower())

        print("g1:" + str(guess_1),"g2:" +  str(guess_2),"g3:" +  str(guess_3))
        gui.setList([guess_1, guess_2, guess_3])
    except:
        print('Update failed')

def keyLoop():
    while True:
        waitForKey()
        update()

def waitForKey():
    key = keyboard.read_key()
    keyboard.on_release_key(key,doNothing)

def doNothing(self):
    pass

def main():
    gui.bindCallback(update)

    word_predictor.process_file("new_corpus.txt")
    word_predictor.create_token_dict()
    word_predictor.create_bigram()
    word_predictor.create_trigram()
    keyThread = threading.Thread(target = keyLoop)
    keyThread.daemon = True
    keyThread.start()
    gui.root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
