from src import wordle_simulator
from src.util import Result
class TestEvaluateGuess:
    def test_evaluateGuess(self):
        answer_word = "rebut"
        guess_word = "saree"
        
        expected_output = [Result.INCORRECT,
                           Result.INCORRECT,
                           Result.MISPLACED,
                           Result.MISPLACED,
                           Result.INCORRECT]
        
        assert wordle_simulator.evaluate_guess(answer_word, guess_word) == expected_output
        
    def test_evaluateGuess1(self):
        answer_word = "rebut"
        guess_word = "civet"
        
        
        expected_output = [Result.INCORRECT,
                           Result.INCORRECT,
                           Result.INCORRECT,
                           Result.MISPLACED,
                           Result.CORRECT]
        
        
        assert wordle_simulator.evaluate_guess(answer_word, guess_word) == expected_output
        
    def test_evaluateGuess2(self):
        answer_word = "organ"
        guess_word = "spoon"
        
        
        expected_output = [Result.INCORRECT,
                           Result.INCORRECT,
                           Result.MISPLACED,
                           Result.INCORRECT,
                           Result.CORRECT]
        
        
        assert wordle_simulator.evaluate_guess(answer_word, guess_word) == expected_output
    # def test_allSameCharacters(self):
