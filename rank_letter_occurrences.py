""" Start off by ranking the occurances of all letters """

# eng_file = open('dict_5_letters.txt', 'r')
# english_dictionary_list = eng_file.read().splitlines()

# ranked_letter_dict = {
#     'a': [0, 0, 0, 0, 0], 
#     'b': [0, 0, 0, 0, 0], 
#     'c': [0, 0, 0, 0, 0], 
#     'd': [0, 0, 0, 0, 0], 
#     'e': [0, 0, 0, 0, 0], 
#     'f': [0, 0, 0, 0, 0], 
#     'g': [0, 0, 0, 0, 0], 
#     'h': [0, 0, 0, 0, 0], 
#     'i': [0, 0, 0, 0, 0], 
#     'j': [0, 0, 0, 0, 0], 
#     'k': [0, 0, 0, 0, 0], 
#     'l': [0, 0, 0, 0, 0], 
#     'm': [0, 0, 0, 0, 0], 
#     'n': [0, 0, 0, 0, 0], 
#     'o': [0, 0, 0, 0, 0], 
#     'p': [0, 0, 0, 0, 0], 
#     'q': [0, 0, 0, 0, 0], 
#     'r': [0, 0, 0, 0, 0], 
#     's': [0, 0, 0, 0, 0], 
#     't': [0, 0, 0, 0, 0], 
#     'u': [0, 0, 0, 0, 0], 
#     'v': [0, 0, 0, 0, 0], 
#     'w': [0, 0, 0, 0, 0], 
#     'x': [0, 0, 0, 0, 0], 
#     'y': [0, 0, 0, 0, 0], 
#     'z': [0, 0, 0, 0, 0], 
# }

# for word in english_dictionary_list:
#     for index, letter in enumerate(word):
#         ranked_letter_dict[letter][index] += 1

# print(ranked_letter_dict)

# ranked_letter_dict = {
#     'a': [1698, 4103, 1959, 2214, 2362], 
#     'b': [1544, 171, 661, 422, 129], 
#     'c': [1499, 329, 695, 761, 295], 
#     'd': [1122, 239, 773, 816, 913], 
#     'e': [693, 2863, 1421, 3252, 2679], 
#     'f': [841, 71, 268, 275, 142], 
#     'g': [958, 138, 614, 610, 256], 
#     'h': [837, 917, 331, 420, 634], 
#     'i': [473, 2239, 1668, 1963, 910], 
#     'j': [446, 32, 81, 61, 10], 
#     'k': [787, 137, 406, 628, 500], 
#     'l': [1040, 1180, 1594, 1285, 965], 
#     'm': [1217, 322, 873, 598, 403], 
#     'n': [641, 669, 1743, 1381, 1512], 
#     'o': [532, 3069, 1426, 1282, 857], 
#     'p': [1178, 331, 553, 510, 275], 
#     'q': [93, 24, 31, 5, 9], 
#     'r': [940, 1529, 2188, 1216, 1186], 
#     's': [2185, 328, 1008, 932, 3737], 
#     't': [1254, 398, 1042, 1369, 1274], 
#     'u': [420, 1824, 990, 899, 247], 
#     'v': [403, 122, 417, 258, 41], 
#     'w': [590, 223, 346, 190, 122], 
#     'x': [32, 83, 169, 25, 144], 
#     'y': [225, 423, 350, 265, 2099], 
#     'z': [175, 59, 216, 186, 122]
#     }

# unordered_by_index = {
#     0: [],
#     1: [],
#     2: [],
#     3: [],
#     4: [],
# }

# n_words_total = 21828

# sum = 0
# for letter, occurance_array in ranked_letter_dict.items():
#     # print(occurance_array) 
#     for index, occurance_quantity in enumerate(occurance_array):
#         unordered_by_index[index].append([letter, occurance_quantity])

# print(unordered_by_index)


# print(unordered_by_index)

# unordered_by_index = {
#     0: [['a', 1698], ['b', 1544], ['c', 1499], ['d', 1122], ['e', 693], ['f', 841], ['g', 958], ['h', 837], ['i', 473], ['j', 446], ['k', 787], ['l', 1040], ['m', 1217], ['n', 641], ['o', 532], ['p', 1178], ['q', 93], ['r', 940], ['s', 2185], ['t', 1254], ['u', 420], ['v', 403], ['w', 590], ['x', 32], ['y', 225], ['z', 175]], 
#     1: [['a', 4103], ['b', 171], ['c', 329], ['d', 239], ['e', 2863], ['f', 71], ['g', 138], ['h', 917], ['i', 2239], ['j', 32], ['k', 137], ['l', 1180], ['m', 322], ['n', 669], ['o', 3069], ['p', 331], ['q', 24], ['r', 1529], ['s', 328], ['t', 398], ['u', 1824], ['v', 122], ['w', 223], ['x', 83], ['y', 423], ['z', 59]], 
#     2: [['a', 1959], ['b', 661], ['c', 695], ['d', 773], ['e', 1421], ['f', 268], ['g', 614], ['h', 331], ['i', 1668], ['j', 81], ['k', 406], ['l', 1594], ['m', 873], ['n', 1743], ['o', 1426], ['p', 553], ['q', 31], ['r', 2188], ['s', 1008], ['t', 1042], ['u', 990], ['v', 417], ['w', 346], ['x', 169], ['y', 350], ['z', 216]], 
#     3: [['a', 2214], ['b', 422], ['c', 761], ['d', 816], ['e', 3252], ['f', 275], ['g', 610], ['h', 420], ['i', 1963], ['j', 61], ['k', 628], ['l', 1285], ['m', 598], ['n', 1381], ['o', 1282], ['p', 510], ['q', 5], ['r', 1216], ['s', 932], ['t', 1369], ['u', 899], ['v', 258], ['w', 190], ['x', 25], ['y', 265], ['z', 186]], 
#     4: [['a', 2362], ['b', 129], ['c', 295], ['d', 913], ['e', 2679], ['f', 142], ['g', 256], ['h', 634], ['i', 910], ['j', 10], ['k', 500], ['l', 965], ['m', 403], ['n', 1512], ['o', 857], ['p', 275], ['q', 9], ['r', 1186], ['s', 3737], ['t', 1274], ['u', 247], ['v', 41], ['w', 122], ['x', 144], ['y', 2099], ['z', 122]]}

# def bubble_sort(array):
#     n = len(array)

#     for i in range(n):
#         # Create a flag that will allow the function to
#         # terminate early if there's nothing left to sort
#         already_sorted = True

#         # Start looking at each item of the list one by one,
#         # comparing it with its adjacent value. With each
#         # iteration, the portion of the array that you look at
#         # shrinks because the remaining items have already been
#         # sorted.
#         for j in range(n - i - 1):
#             if array[j][1] < array[j + 1][1]:
#                 # If the item you're looking at is greater than its
#                 # adjacent value, then swap them
#                 array[j], array[j + 1] = array[j + 1], array[j]

#                 # Since you had to swap two elements,
#                 # set the `already_sorted` flag to `False` so the
#                 # algorithm doesn't finish prematurely
#                 already_sorted = False

#         # If there were no swaps during the last iteration,
#         # the array is already sorted, and you can terminate
#         if already_sorted:
#             break

#     return array

# test = [['a', 1698], ['b', 1544], ['c', 1499], ['d', 1122], ['e', 693], ['f', 841], ['g', 958], ['h', 837], ['i', 473], ['j', 446], ['k', 787], ['l', 1040], ['m', 1217], ['n', 641], ['o', 532], ['p', 1178], ['q', 93], ['r', 940], ['s', 2185], ['t', 1254], ['u', 420], ['v', 403], ['w', 590], ['x', 32], ['y', 225], ['z', 175]]
# print(bubble_sort(test))

# ordered_by_index = {}

# for index, values_array in unordered_by_index.items():
#     ordered_by_index[index] = bubble_sort(values_array)

# print(ordered_by_index)


# ordered_by_index = {
#     1: [['s', 2185], ['a', 1698], ['b', 1544], ['c', 1499], ['t', 1254], ['m', 1217], ['p', 1178], ['d', 1122], ['l', 1040], ['g', 958], ['r', 940], ['f', 841], ['h', 837], ['k', 787], ['e', 693], ['n', 641], ['w', 590], ['o', 532], ['i', 473], ['j', 446], ['u', 420], ['v', 403], ['y', 225], ['z', 175], ['q', 93], ['x', 32]], 
#     2: [['a', 4103], ['o', 3069], ['e', 2863], ['i', 2239], ['u', 1824], ['r', 1529], ['l', 1180], ['h', 917], ['n', 669], ['y', 423], ['t', 398], ['p', 331], ['c', 329], ['s', 328], ['m', 322], ['d', 239], ['w', 223], ['b', 171], ['g', 138], ['k', 137], ['v', 122], ['x', 83], ['f', 71], ['z', 59], ['j', 32], ['q', 24]], 
#     3: [['r', 2188], ['a', 1959], ['n', 1743], ['i', 1668], ['l', 1594], ['o', 1426], ['e', 1421], ['t', 1042], ['s', 1008], ['u', 990], ['m', 873], ['d', 773], ['c', 695], ['b', 661], ['g', 614], ['p', 553], ['v', 417], ['k', 406], ['y', 350], ['w', 346], ['h', 331], ['f', 268], ['z', 216], ['x', 169], ['j', 81], ['q', 31]], 
#     4: [['e', 3252], ['a', 2214], ['i', 1963], ['n', 1381], ['t', 1369], ['l', 1285], ['o', 1282], ['r', 1216], ['s', 932], ['u', 899], ['d', 816], ['c', 761], ['k', 628], ['g', 610], ['m', 598], ['p', 510], ['b', 422], ['h', 420], ['f', 275], ['y', 265], ['v', 258], ['w', 190], ['z', 186], ['j', 61], ['x', 25], ['q', 5]], 
#     5: [['s', 3737], ['e', 2679], ['a', 2362], ['y', 2099], ['n', 1512], ['t', 1274], ['r', 1186], ['l', 965], ['d', 913], ['i', 910], ['o', 857], ['h', 634], ['k', 500], ['m', 403], ['c', 295], ['p', 275], ['g', 256], ['u', 247], ['x', 144], ['f', 142], ['b', 129], ['w', 122], ['z', 122], ['v', 41], ['j', 10], ['q', 9]]}

# eng_file = open('dict_5_letters.txt', 'r')
# english_dictionary_list = eng_file.read().splitlines()

# print('trying')
# english_dictionary_list = ['train']


# ranked_letter_dict = {
#     'a': [1698, 4103, 1959, 2214, 2362], 
#     'b': [1544, 171, 661, 422, 129], 
#     'c': [1499, 329, 695, 761, 295], 
#     'd': [1122, 239, 773, 816, 913], 
#     'e': [693, 2863, 1421, 3252, 2679], 
#     'f': [841, 71, 268, 275, 142], 
#     'g': [958, 138, 614, 610, 256], 
#     'h': [837, 917, 331, 420, 634], 
#     'i': [473, 2239, 1668, 1963, 910], 
#     'j': [446, 32, 81, 61, 10], 
#     'k': [787, 137, 406, 628, 500], 
#     'l': [1040, 1180, 1594, 1285, 965], 
#     'm': [1217, 322, 873, 598, 403], 
#     'n': [641, 669, 1743, 1381, 1512], 
#     'o': [532, 3069, 1426, 1282, 857], 
#     'p': [1178, 331, 553, 510, 275], 
#     'q': [93, 24, 31, 5, 9], 
#     'r': [940, 1529, 2188, 1216, 1186], 
#     's': [2185, 328, 1008, 932, 3737], 
#     't': [1254, 398, 1042, 1369, 1274], 
#     'u': [420, 1824, 990, 899, 247], 
#     'v': [403, 122, 417, 258, 41], 
#     'w': [590, 223, 346, 190, 122], 
#     'x': [32, 83, 169, 25, 144], 
#     'y': [225, 423, 350, 265, 2099], 
#     'z': [175, 59, 216, 186, 122]
#     }

# word_rank_dict = {}

# for word in english_dictionary_list:
#     for index, character in enumerate(word):
#         if word in word_rank_dict:
#             word_rank_dict[word] += ranked_letter_dict[character][index]
#         else:
#             word_rank_dict[word] = ranked_letter_dict[character][index]


# print(word_rank_dict)

# result = dict(sorted(word_rank_dict.items(), key=lambda item: item[1]))

""" Creating the JSON file of all the words ranked """

# import json
    
# # Data to be written
# dictionary ={
#     "name" : "sathiyajith",
#     "rollno" : 56,
#     "cgpa" : 8.6,
#     "phonenumber" : "9976770500"
# }
    
# with open("words_ranked.json", "w") as outfile:
#     json.dump(result, outfile)

""" Reading the user input and refining the list of possible words """
import enum
import json
file = open('words_ranked.json')
word_length: int = 5

def contains_bad_characters(word, bad_characters) -> bool:
    for character in bad_characters:
        if character == '*': 
            continue
        if character in word:
            return True
    return False

def matches_good_characters(word, good_characters) -> bool:
    for index in range(word_length):
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

    # for index, character_array in enumerate(possible_characters):
    #     for character in character_array:
    #         if word[index] == character:
    #             return False
    #         if character not in word:
    #             return False
    # return True


def filter_possible_words(current_ranked_words, good_characters, possible_characters, bad_characters):
    filtered_ranked_words = []
    for word in current_ranked_words:
        # print(word)
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
        characters = input(f'Enter {characters_type} characters: ')    
    return characters

def get_all_inputs():
    """ Gets user input """
    good_characters = get_a_input('good')
    possible_characters = get_a_input('possible')
    bad_characters = get_a_input('bad')
    return good_characters, possible_characters, bad_characters

# good_characters, possible_characters, bad_characters =  get_input()


def main():
    current_ranked_words = list(json.load(file).keys())

    while len(current_ranked_words) > 1:
        print(current_ranked_words)
        good_characters, possible_characters, bad_characters =  get_all_inputs()
        current_ranked_words = filter_possible_words(current_ranked_words, good_characters, possible_characters, bad_characters)

main()
# print(good_characters)
# print(possible_characters)
# print(bad_characters)