import sys
from typing import List
from enum import Enum

class Result(Enum):
    CORRECT = 0
    INCORRECT = 1
    MISPLACED = 2

def exit_program():
    print("Exiting the progam")
    sys.exit(1)


def read_txt_file(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file '{file_path}': {e}")

    exit_program()