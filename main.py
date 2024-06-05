from src import util, solver, wordle_simulator
from typing import List
import numpy as np

def run_user_input():
   # n_guesses: int = 0
    # def test_one(self):
        # pdb.set_trace()
    # result = [('b', Result.INCORRECT),
    #             ('o', Result.INCORRECT),
    #             ('n', Result.INCORRECT),
    #             ('n', Result.CORRECT),
    #             ('y', Result.INCORRECT)]
    
    # word_to_test = "flint"
    # print(word_meets_all_criteria(word_to_test, result))



    MASTER_WORDS = util.read_txt_file("master_words.txt")
    possible_valid_words = util.read_txt_file("wordle_words.txt")
    used_letters = ""
    guess_number = 1

    while len(possible_valid_words) > 0:
        best_suggestion = solver.suggest_best_guess(MASTER_WORDS, possible_valid_words, used_letters)
        solver.display_guessing_information(best_suggestion, guess_number, possible_valid_words)
        guessed_word, guess_results = solver.get_guess_results_from_input(best_suggestion)
        used_letters = used_letters + guessed_word
        possible_valid_words = solver.filter_possible_valid_words(possible_valid_words, guessed_word, guess_results)
        print(possible_valid_words)
        guess_number += 1


def present_results(results: dict[int, List[str]]):
    sum1 = 0
    n_words_guessed = 0
    for key, value in results.items():
        n_words_guessed += len(value)
        sum1 += key * len(value)

    print(results)
    print(sum1)
    print(sum1/n_words_guessed)

    

def run_simulation():
    MASTER_WORDS = util.read_txt_file("master_words.txt")
    answer_words = util.read_txt_file("wordle_words.txt")
    wordle_words = util.read_txt_file("wordle_words.txt")
    
    results = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    
    # answer_word = answer_words[50]
    # answer_word = "booby"
    for i, answer_word in enumerate(answer_words):
        n_guesses = wordle_simulator.simulate_wordle(answer_word, MASTER_WORDS, wordle_words)
        results[n_guesses].append(answer_word)
        print(f"{i}")
        
    present_results(results)
    
    

def main():
    run_simulation()
    # run_user_input()
    

if __name__ == "__main__":
    main()


# print('hello world')
# util.exit_program()