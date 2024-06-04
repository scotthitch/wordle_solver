import pytest
from src import solver


class TestCorrrectCharCriteriaMet:
    # Test for multiple locations

    # Could make tests for if index out of range but ceebs

    def test_charInWordSameIndex_assertTrue(self):
        char = 'a'
        index = 3
        word = "plead"

        assert solver.correct_char_criteria_met(char, index, word) == True

    def test_charInWordDifferentIndex_assertFalse(self):
        char = 'b'
        index = 1
        word = "bribe"

        assert solver.correct_char_criteria_met(char, index, word) == False

    def test_charNotInWord_assertFalse(self):
        char = 'z'
        index = 0
        word = "bring"

        assert solver.correct_char_criteria_met(char, index, word) == False


class TestIncorrrectCharCriteriaMet:
    # Test for multiple locations

    def test_charNotInWord_assertTrue(self):
        char = 'z'
        word = "bring"

        assert solver.incorrect_char_criteria_met(char, word) == True

    def test_charInWord_assertFalse(self):
        char = 'a'
        word = "plead"

        assert solver.incorrect_char_criteria_met(char, word) == False


class TestMisplacedCharCriteriaMet:
    # Test for multiple locations
    def test_charInDifferentIndex_assertTrue(self):
        char = 'g'
        index = 2
        word = "bring"

        assert solver.misplaced_char_criteria_met(char, index, word) == True

    def test_charInDifferentIndexAndOthers_assertTrue(self):
        char = 'i'
        index = 0
        word = "limit"
        
        assert solver.misplaced_char_criteria_met(char, index, word) == True

    def test_charInSameIndex_assertFalse(self):
        char = 'n'
        index = 3
        word = "think"

        assert solver.misplaced_char_criteria_met(char, index, word) == False

    def test_charInSameIndexAndOthers_assertFalse(self):
        char = 'e'
        index = 1
        word = "fewer"
        
        assert solver.misplaced_char_criteria_met(char, index, word) == False

    def test_charNotInWord_assertFalse(self):
        char = 'p'
        index = 3
        word = "eager"

        assert solver.misplaced_char_criteria_met(char, index, word) == False

# class TestWordMeetsCriteria:
#     def test_one(self):
#         result = [('b', solver.Result.INCORRECT),
#                   ('o', solver.Result.INCORRECT),
#                   ('n', solver.Result.INCORRECT),
#                   ('n', solver.Result.CORRECT),
#                   ('y', solver.Result.INCORRECT)]
        
#         word_to_test = "flint"
#         assert solver.word_meets_all_criteria(word_to_test, result) == True

    # def test_two(self):
    #     result = [('g', solver.Result.CORRECT),
    #               ('r', solver.Result.CORRECT),
    #               ('o', solver.Result.CORRECT),
    #               ('i', solver.Result.INCORRECT),
    #               ('n', solver.Result.INCORRECT)]
        
    #     word_to_test = "groom"
    #     assert solver.word_meets_all_criteria(word_to_test, result) == True


    # def test_three(self):
    #     result = [('r', solver.Result.CORRECT),
    #               ('o', solver.Result.MISPLACED),
    #               ('m', solver.Result.INCORRECT),
    #               ('a', solver.Result.MISPLACED),
    #               ('n', solver.Result.CORRECT)]
    
    #     word_to_test = "champ"
    #     assert solver.word_meets_all_criteria(word_to_test, result) == False


    # def test_four(self):
    #     result = [('c', solver.Result.INCORRECT),
    #               ('h', solver.Result.INCORRECT),
    #               ('a', solver.Result.MISPLACED),
    #               ('m', solver.Result.INCORRECT),
    #               ('p', solver.Result.INCORRECT)]
    
    #     word_to_test = "frame"
    #     assert solver.word_meets_all_criteria(word_to_test, result) == False

    
    # def test_five(self):
    #     result = [('b', solver.Result.INCORRECT),
    #               ('r', solver.Result.INCORRECT),
    #               ('i', solver.Result.INCORRECT),
    #               ('n', solver.Result.INCORRECT),
    #               ('g', solver.Result.INCORRECT)]
    
    #     word_to_test = "think"
    #     assert solver.word_meets_all_criteria(word_to_test, result) == False

    # def test_six(self):
    #     result = [('t', solver.Result.INCORRECT),
    #               ('h', solver.Result.INCORRECT),
    #               ('i', solver.Result.INCORRECT),
    #               ('n', solver.Result.INCORRECT),
    #               ('k', solver.Result.INCORRECT)]
    
    #     word_to_test = "plead"
    #     assert solver.word_meets_all_criteria(word_to_test, result) == True


    # def test_seven(self):
    #     result = [('b', solver.Result.INCORRECT),
    #               ('l', solver.Result.MISPLACED),
    #               ('e', solver.Result.INCORRECT),
    #               ('a', solver.Result.CORRECT),
    #               ('k', solver.Result.INCORRECT)]
    
    #     word_to_test = "reads"
    #     assert solver.word_meets_all_criteria(word_to_test, result) == False