import string
from typing import List
from . import util
from .util import Result, WORD_LENGTH
# from . import plotting

def rank_letters(words_list: list, used_letters: str) -> dict:
    # letters_ranked = {}
    letters_ranked = {letter: [0,0,0,0,0] for letter in string.ascii_lowercase}


    for word in words_list:
        for i, character in enumerate(word):
            if character not in used_letters:
                letters_ranked[character][i] += 1
    return letters_ranked

def score_words(words_list: list, ranked_letters: dict) -> dict:
    words_score = {}
    
    for word in words_list:
        words_score[word] = 0
        
        for i, character in enumerate(word):
            if character not in ranked_letters: 
                continue

            words_score[word] += ranked_letters[character][i]
    return words_score


def correct_char_criteria_met(char: str, index: int, word: str):
    return char == word[index]

def incorrect_char_criteria_met(char: str, word: str):
    return char not in word

def misplaced_char_criteria_met(char: str, index: int, word: str):
    return char != word[index] and char in word

def word_meets_all_criteria(word: str, guessed_word, guess_results):
    # Loop through all characters in word and check that each criteria is met
    for i, (char, char_result) in enumerate(zip(guessed_word, guess_results)):
        if char_result == Result.CORRECT:
            if not correct_char_criteria_met(char, i, word):
                return False
            word = util.replace_char_at_index(word, "_", i)
            
    for i, (char, char_result) in enumerate(zip(guessed_word, guess_results)):
        if char_result == Result.MISPLACED:
            if not misplaced_char_criteria_met(char, i, word):
                return False
            word = word.replace(char, '_')


    for i, (char, char_result) in enumerate(zip(guessed_word, guess_results)):
        if char_result == Result.INCORRECT:
            if not incorrect_char_criteria_met(char, word):
                return False
            
    return True

def filter_possible_valid_words(current_possible_words: list, guessed_word: str, guess_results: List[Result]):
    filtered_ranked_words = []
    for word in current_possible_words:
        if (word_meets_all_criteria(word, guessed_word, guess_results)):
            filtered_ranked_words.append(word)
    return filtered_ranked_words

def suggest_best_guess(master_words: list[str], possible_words: list[str], used_letters: str) -> str:
    if (len(possible_words) <= 2):
        return possible_words[0]
    
    letters_ranked = rank_letters(possible_words, used_letters)
    words_ranked = score_words(master_words, letters_ranked)
    
    best_guess = max(words_ranked, key=words_ranked.get)
    # plotting.plot_letter_distribution(letters_ranked, best_guess)
    return best_guess


def display_guessing_information(best_suggestion: str, guess_number: int, possible_valid_words: list[str]):
    print("\n----------------")
    print(f"Guess {guess_number}")
    print("----------------\n")
    if (len(possible_valid_words) > 1):
        print(f"There are {len(possible_valid_words)} possible words left")
        print(f"Next best guess is '{best_suggestion}'\n")
    else:
        print(f"The solution is '{possible_valid_words[0]}'\n")
        

def get_guessed_word():
    guess = ''
    while (len(guess) != WORD_LENGTH):
        guess = input('Enter guessed word: ')    
    return guess

def get_results() -> list[Result]:
    user_input = input("Enter results from the word (c: correct, i: incorrect, m: misplaced) ")

    # Check the length is WORD_LENGTH or else call it again
    if len(user_input) != WORD_LENGTH:
        print(f"String length must be {WORD_LENGTH}.")
        return get_results()
    

    # Build results array using enums 
    # Check all inputs are 'w', 'c' or 'm' or else call it again
    results = []
    for char in user_input:
        match char:
            case 'c':
                results.append(Result.CORRECT)
            case 'i':
                results.append(Result.INCORRECT)
            case 'm':
                results.append(Result.MISPLACED)
            case _:
                print("Invalid character. Only 'c', 'i', or 'm' are allowed.")
                return get_results()
    
    return results

def get_guess_results_from_input(best_suggestion):
    # guessed_word = get_guessed_word()
    guessed_word = best_suggestion
    results = get_results()

    if (len(guessed_word) != WORD_LENGTH or len(results) != WORD_LENGTH):
        print(f"Somehow lengths aren't {WORD_LENGTH}")
        util.exit_program()

    
    # result_array_tuple = []
    # for i in range(len(guessed_word)):
    #     result_array_tuple.append((guessed_word[i], results[i]))
    
    return guessed_word, results