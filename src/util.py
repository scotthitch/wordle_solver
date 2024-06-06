import sys
from typing import List
from enum import Enum

WORD_LENGTH: int = 5

class Result(Enum):
    CORRECT = 0
    INCORRECT = 1
    MISPLACED = 2

def exit_program():
    print("Exiting the progam")
    sys.exit(1)


def read_txt_file_resource(file_name: str) -> List[str]:
    file_path = f"resources/{file_name}"
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
        
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file '{file_name}': {e}")

    exit_program()
    
    
def replace_char_at_index(original_str: str, new_char: str, index: int):
    new_str = original_str[:index] + new_char + original_str[index+1:]
    return new_str

def is_char_first_occurance(word: str, index: int):
    return word[index] not in word[:index]