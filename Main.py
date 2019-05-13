from WordPredictor import WordPredictor
from gui import GUI
import threading
gui = GUI()
def second_main():
    word_predictor = WordPredictor()
    word_predictor.process_file("corpus.txt")
    user_input = gui.getText()
    user_input = user_input[:-1]
    print('user input: ' + user_input)
    print('user input[-1]:' + user_input[-1] + 'end')
    user_word_list = user_input.split()

    # guess next full word using previous word
    if user_input[-1] == " " and len(user_word_list) == 1:
        print('here1')
        word_predictor.create_bigram()
        guess_1, guess_2, guess_3 = word_predictor.guess_next_word_bigram(user_word_list[0])

    # guess next full word using past 2 words
    elif user_input[-1] == " " and len(user_word_list) >= 2:
        word_predictor.create_trigram()
        print(user_word_list[-2], user_word_list[-1])
        guess_1, guess_2, guess_3 = word_predictor.guess_next_word_trigram(user_word_list[-2], user_word_list[-1])

    # guess ending of current word
    else:
        guess_1, guess_2, guess_3 = word_predictor.finish_word(user_word_list[-1].lower())
    gui.setList([guess_1, guess_2, guess_3])
    print(guess_1, guess_2, guess_3)

def main():
    second_main_thread = threading.Thread(target = second_main)
    second_main_thread.start()
    gui.root.mainloop()


if __name__ == "__main__":
    main()
