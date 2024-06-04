import pytest
from src import solver


class TestWordMeetsCriteria:
    def test_one():
        result = [('s', solver.Result.INCORRECT),
                ('l', solver.Result.INCORRECT),
                ('a', solver.Result.INCORRECT),
                ('t', solver.Result.INCORRECT),
                ('e', solver.Result.INCORRECT)]
        
        word_to_test = "groin"
        assert solver.word_meets_criteria(word_to_test, result)


    def test_two():
        result = [('s', solver.Result.INCORRECT),
                ('l', solver.Result.INCORRECT),
                ('a', solver.Result.INCORRECT),
                ('t', solver.Result.INCORRECT),
                ('e', solver.Result.INCORRECT)]
        
        word_to_test = "guild"
        assert solver.word_meets_criteria(word_to_test, result) != True