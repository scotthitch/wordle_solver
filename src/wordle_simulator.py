from . import solver
from .util import Result, WORD_LENGTH, replace_char_at_index
from typing import List


def evaluate_guess(answer_word: str, guess: str):

    # letters_ranked = {letter: [0,0,0,0,0] for letter in string.ascii_lowercase}

    # print(test_word)
    # print(guess)
    results = [Result.INCORRECT] * WORD_LENGTH
    # print(results)

    for i, char in enumerate(guess):
        if char == answer_word[i]:
            results[i] = Result.CORRECT
            answer_word = replace_char_at_index(answer_word, '_', i)
            
    for i, char in enumerate(guess):
        if char in answer_word:
            results[i] = Result.MISPLACED
            index_first_occurance = answer_word.find(char)
            answer_word = replace_char_at_index(answer_word, '_', index_first_occurance)

    # for i, char in enumerate(answer_word):
    #     # if char not in test_word:
    #     if char in guess:
    #         results[i] = Result.MISPLACED

    #     if char == guess[i]:
    #         results[i] = Result.CORRECT
    # print(results)
    
    return results

def simulate_wordle(test_word: str, MASTER_WORDS: List[str], possible_words: List[str]) -> int:
    # return
    guess_number = 1
    used_letters = ""    

    while len(possible_words) > 1:
        best_suggestion = solver.suggest_best_guess(MASTER_WORDS, possible_words, used_letters)
        # solver.display_guessing_information(best_suggestion, guess_number, possible_words)
        guess_results = evaluate_guess(test_word, best_suggestion)
        # guess_results = solver.get_guess_results_from_input(best_suggestion)
        used_letters = used_letters + best_suggestion
        # possible_words = solver.filter_possible_valid_words(possible_words, guess_results)
        possible_words = solver.filter_possible_valid_words(possible_words, best_suggestion, guess_results)
        
        guess_number += 1
        
    return guess_number