import pytest
from src import solver


class TestWordMeetsCriteria:
    def test_one(self):
        result = [('s', solver.Result.INCORRECT),
                  ('l', solver.Result.INCORRECT),
                  ('a', solver.Result.INCORRECT),
                  ('t', solver.Result.INCORRECT),
                  ('e', solver.Result.INCORRECT)]
        
        word_to_test = "groin"
        assert solver.word_meets_criteria(word_to_test, result) == True

    def test_two(self):
        result = [('g', solver.Result.CORRECT),
                  ('r', solver.Result.CORRECT),
                  ('o', solver.Result.CORRECT),
                  ('i', solver.Result.INCORRECT),
                  ('n', solver.Result.INCORRECT)]
        
        word_to_test = "groom"
        assert solver.word_meets_criteria(word_to_test, result) == True


    def test_three(self):
        result = [('r', solver.Result.CORRECT),
                  ('o', solver.Result.MISPLACED),
                  ('m', solver.Result.INCORRECT),
                  ('a', solver.Result.MISPLACED),
                  ('n', solver.Result.CORRECT)]
    
        word_to_test = "champ"
        assert solver.word_meets_criteria(word_to_test, result) == False


    def test_four(self):
        result = [('c', solver.Result.INCORRECT),
                  ('h', solver.Result.INCORRECT),
                  ('a', solver.Result.MISPLACED),
                  ('m', solver.Result.INCORRECT),
                  ('p', solver.Result.INCORRECT)]
    
        word_to_test = "frame"
        assert solver.word_meets_criteria(word_to_test, result) == False

    
    def test_five(self):
        result = [('b', solver.Result.INCORRECT),
                  ('r', solver.Result.INCORRECT),
                  ('i', solver.Result.INCORRECT),
                  ('n', solver.Result.INCORRECT),
                  ('g', solver.Result.INCORRECT)]
    
        word_to_test = "think"
        assert solver.word_meets_criteria(word_to_test, result) == False

    def test_six(self):
        result = [('t', solver.Result.INCORRECT),
                  ('h', solver.Result.INCORRECT),
                  ('i', solver.Result.INCORRECT),
                  ('n', solver.Result.INCORRECT),
                  ('k', solver.Result.INCORRECT)]
    
        word_to_test = "plead"
        assert solver.word_meets_criteria(word_to_test, result) == True


    def test_seven(self):
        result = [('b', solver.Result.INCORRECT),
                  ('l', solver.Result.MISPLACED),
                  ('e', solver.Result.INCORRECT),
                  ('a', solver.Result.CORRECT),
                  ('k', solver.Result.INCORRECT)]
    
        word_to_test = "reads"
        assert solver.word_meets_criteria(word_to_test, result) == False