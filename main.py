from calendar import c
from collections import Counter
import sys

WORD_LENGTH: int = 5

def exit_program():
    print("Exiting the progam")
    sys.exit(1)


def read_txt_file(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file '{file_path}': {e}")

    exit_program()    

def rank_letters(words_list: list, used_letters: list) -> dict:
    letters_ranked = {}

    for word in words_list:
        for character in word:
            if character in used_letters:
                letters_ranked[character] = 0
                continue

            if character not in letters_ranked:
                letters_ranked[character] = 1
                
            else:
                letters_ranked[character] += 1

    return letters_ranked

def rank_words(words_list: list, ranked_letters: dict) -> dict:
    words_ranked = {}
    for word in words_list:
        for character in word:
            if character not in ranked_letters: 
                continue

            if word not in words_ranked:
                words_ranked[word] = ranked_letters[character]
                continue

            words_ranked[word] += ranked_letters[character]
    return words_ranked


def word_has_unique_chars(word) -> bool:
    frequency = Counter(word)
 
    if(len(frequency) == len(word)):
        return True
    else:
        return False

# def word

def find_best_word(ranked_words_list: list) -> str:
    for word in reversed(ranked_words_list):
        if word_has_unique_chars(word):
            return word



def matches_good_characters(word, good_characters) -> bool:
    for index in range(WORD_LENGTH):
        if good_characters[index] == '*': 
            continue

        if good_characters[index] != word[index]:
            return False

    return True 
        

def contains_possible_characters(word, possible_characters) -> bool:
    """ Checks if the words contains each character but not in that exact position """
    for index, character in enumerate(possible_characters):
        if character == '*':
            continue

        if character == word[index]:
            return False

        if character not in word:
            return False

    return True


def contains_bad_characters(word, bad_characters) -> bool:
    for character in bad_characters:
        if character == '*': 
            continue

        if character in word:
            return True

    return False


def filter_possible_words(current_ranked_words: list, good_characters: str, possible_characters: str, bad_characters: str):
    filtered_ranked_words = []
    for word in current_ranked_words:
        if contains_bad_characters(word, bad_characters): 
            continue
        
        if not(matches_good_characters(word, good_characters)):
            continue

        if not(contains_possible_characters(word, possible_characters)):
            continue

        filtered_ranked_words.append(word)
    return filtered_ranked_words

def build_guessing_words_sorted_list(possible_words_list: list, master_word_list: list, used_letters: list) -> list:
    letters_ranked = rank_letters(possible_words_list, used_letters)
    words_ranked = rank_words(master_word_list, letters_ranked)
    return list((dict(sorted(words_ranked.items(), key=lambda item: item[1]))).keys())


def build_master_words_sorted_as_list(dictionary_list: list, used_letters: list) -> list:
    letters_ranked = rank_letters(dictionary_list, used_letters)
    words_ranked = rank_words(dictionary_list, letters_ranked)
    return list((dict(sorted(words_ranked.items(), key=lambda item: item[1]))).keys())


def display_information(guessing_words_list: list, possible_words_list: list, guess_number: int):
    print("\n----------------")
    print(f"Guess {guess_number}")
    print("----------------\n")
    print("Possible words: ")
    print(possible_words_list, '\n')
    print(f'Possible words remaining: {len(possible_words_list)}')
    
    
    for word in reversed(guessing_words_list):       
        
        if word_has_unique_chars(word):
            if word not in wordle_master_words:
                continue

            print(f'Best guess is: {word}')

            
            # if input('Valid word? y/n ') == 'y':
            return word
    print(f'Best guess is: {guessing_words_list[-1]}')
    return guessing_words_list[-1]


def get_a_input(characters_type: str):
    characters = ''
    while (len(characters) != 5):
        characters = input(f'Enter 5 {characters_type} characters: ')    
    return characters


def get_all_inputs(best_guess_word: str):
    """ Gets user input """
    good_characters = ['*', '*', '*', '*', '*']
    possible_characters = ['*', '*', '*', '*', '*']
    bad_characters = ['*', '*', '*', '*', '*']

    values = ''
    while (len(values) != 5):
        values = input(f'Enter all values: ')    

    for index, value in enumerate(values):
        if value == 'y':
            good_characters[index] = best_guess_word[index]
            continue

        if value == 'm':
            possible_characters[index] = best_guess_word[index]
            continue

        if value == 'n':
            bad_characters[index] = best_guess_word[index]
            continue

    return good_characters, possible_characters, bad_characters

def update_used_indicies(used_indicies: list, good_characters: str) -> list:
    for index, character in enumerate(good_characters):
        if character != '*':
            used_indicies[index] = True
    return used_indicies

def update_used_letters(used_letters: list, good_characters: str, possible_characters: str, bad_characters: str) -> list:
    new_used_letters = used_letters

    for character in good_characters:
        if character != '*':
            new_used_letters.append(character)

    for character in possible_characters:
        if character != '*':
            new_used_letters.append(character)
        
    for character in bad_characters:
        if character != '*':
            new_used_letters.append(character)
        
    return new_used_letters

def main():
    master_words = read_txt_file("master_words.txt")
    wordle_words = read_txt_file("wordle_words.txt")

    # print(len(master_words))
    # print(len(wordle_words))

    # guess_number = 1
    # used_letters = []
    # master_sorted_ranked_word_list = build_master_words_sorted_as_list(wordle_possible_words, used_letters)
    # possible_words_list = master_sorted_ranked_word_list
    # guessing_words_list = master_sorted_ranked_word_list


    # while len(possible_words_list) > 0:
    #     best_guess_word = display_information(guessing_words_list, possible_words_list, guess_number)
    #     good_characters, possible_characters, bad_characters =  get_all_inputs(best_guess_word)
    #     used_letters = update_used_letters(used_letters, good_characters, possible_characters, bad_characters)
    #     possible_words_list = filter_possible_words(possible_words_list, good_characters, possible_characters, bad_characters)
    #     guessing_words_list = build_guessing_words_sorted_list(possible_words_list, master_sorted_ranked_word_list, used_letters)
    #     guess_number += 1

main()