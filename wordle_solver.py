""" Reading the user input and refining the list of possible words """
import json
from collections import Counter

WORD_LENGTH: int = 5

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


def filter_possible_words(current_ranked_words, good_characters, possible_characters, bad_characters):
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


def get_a_input(characters_type: str):
    characters = ''
    while (len(characters) != 5):
        characters = input(f'Enter 5 {characters_type} characters: ')    
    return characters


def get_all_inputs():
    """ Gets user input """
    good_characters = get_a_input('good')
    possible_characters = get_a_input('possible')
    bad_characters = get_a_input('bad')
    return good_characters, possible_characters, bad_characters


def word_has_unique_chars(word) -> bool:
    frequency = Counter(word)
 
    if(len(frequency) == len(word)):
        return True
    else:
        return False


def display_information(current_ranked_words):
    print(current_ranked_words)
    print(f'Possible words remaining: {len(current_ranked_words)}')
    for word in reversed(current_ranked_words):
        if word_has_unique_chars(word):
            print(f'Best guess is: {word}')
            return
    print(f'Best guess is: {current_ranked_words[-1]}')

 
def main():
    file = open('words_ranked.json')
    current_ranked_words = list(json.load(file).keys())

    while len(current_ranked_words) > 1:
        display_information(current_ranked_words)
        good_characters, possible_characters, bad_characters =  get_all_inputs()
        current_ranked_words = filter_possible_words(current_ranked_words, good_characters, possible_characters, bad_characters)

main()
