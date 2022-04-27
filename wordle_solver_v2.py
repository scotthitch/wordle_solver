from collections import Counter
WORD_LENGTH: int = 5


eng_file = open('dict_5_letters.txt', 'r')
english_dictionary_list = eng_file.read().splitlines()

def rank_letters(words_list: list, known_indicies: list) -> dict:
    letters_ranked = {}

    for word in words_list:
        for index, character in enumerate(word):
            if known_indicies[index] == True:
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

def build_words_sorted_as_list(possible_words_list: list, master_word_list: list, known_indicies: list) -> list:
    letters_ranked = rank_letters(possible_words_list, known_indicies)
    words_ranked = rank_words(master_word_list, letters_ranked)
    return list((dict(sorted(words_ranked.items(), key=lambda item: item[1]))).keys())


def build_master_words_sorted_as_list(dictionary_list: list, known_indicies: list) -> list:
    letters_ranked = rank_letters(dictionary_list, known_indicies)
    words_ranked = rank_words(dictionary_list, letters_ranked)
    return list((dict(sorted(words_ranked.items(), key=lambda item: item[1]))).keys())


def display_information(guessing_words_list: list, possible_words_list: list):
    print(guessing_words_list)
    print(possible_words_list)
    print(f'Possible words remaining: {len(possible_words_list)}')
    
    
    for word in reversed(guessing_words_list):       
        
        if word_has_unique_chars(word):
            print(f'Best guess is: {word}')
            if input('Valid word? y/n ') == 'y':
                return
    print(f'Best guess is: {guessing_words_list[-1]}')



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

def update_known_indicies(known_indicies: list, good_characters: str) -> list:
    for index, character in enumerate(good_characters):
        if character != '*':
            known_indicies[index] = True
    return known_indicies


def main():
    known_indicies = [False, False, False, False, False]
    master_sorted_ranked_word_list = build_master_words_sorted_as_list(english_dictionary_list, known_indicies)
    possible_words_list = master_sorted_ranked_word_list
    guessing_words_list = master_sorted_ranked_word_list

    while len(possible_words_list) > 0:
        display_information(guessing_words_list, possible_words_list)
        good_characters, possible_characters, bad_characters =  get_all_inputs()
        known_indicies = update_known_indicies(known_indicies, good_characters)
        possible_words_list = filter_possible_words(possible_words_list, good_characters, possible_characters, bad_characters)
        print(possible_words_list)
        guessing_words_list = build_words_sorted_as_list(possible_words_list, master_sorted_ranked_word_list, known_indicies)


main()