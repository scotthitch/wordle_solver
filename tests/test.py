import pytest
from src import solver

def test_answer():
    result = [('s', solver.Result.INCORRECT),
              ('l', solver.Result.INCORRECT),
              ('a', solver.Result.INCORRECT),
              ('t', solver.Result.INCORRECT),
              ('e', solver.Result.INCORRECT)]
    
    word_to_test = "guild"
    assert solver.word_meets_criteria(word_to_test, result) != True