from src import solver
# from . import util
from typing import List


def evaluate_guess(test_word: str, guess: str):
    pass

def simulate_wordle(test_word: str, MASTER_WORDS: List[str], possible_words: List[str]):
    return
    guess_number = 1
    used_letters = ""


    while len(possible_words) > 0:
        best_suggestion = solver.suggest_best_guess(MASTER_WORDS, possible_words, used_letters)
        solver.display_guessing_information(best_suggestion, guess_number, possible_words)
        guess_results = solver.get_guess_results_from_input(best_suggestion)
        used_letters = used_letters + best_suggestion
        possible_words = solver.filter_possible_valid_words(possible_words, guess_results)
        guess_number += 1
