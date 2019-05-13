from WordPredictor import WordPredictor

def main():
    word_predictor = WordPredictor()
    word_predictor.process_file("corpus.txt")

    user_input = "welcom"
    user_word_list = user_input.split()

    # guess next full word using previous word
    if user_input[-1] == " " and len(user_word_list) == 1:
        word_predictor.create_bigram()
        guess_1, guess_2, guess_3 = word_predictor.guess_next_word_bigram(user_word_list[0])

    # guess next full word using past 2 words
    elif user_input[-1] == " " and len(user_word_list) >= 2:
        word_predictor.create_trigram()
        guess_1, guess_2, guess_3 = word_predictor.guess_next_word_trigram(user_word_list[-2], user_word_list[-1])

    # guess ending of current word
    else:
        guess_1, guess_2, guess_3 = word_predictor.finish_word(user_word_list[-1].lower())

    print(guess_1, guess_2, guess_3)

if __name__ == "__main__":
    main()