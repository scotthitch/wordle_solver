from src import util

class TestCharFirstOccurrence:
    def test_charOccursOnce_assertTrue(self):
        index = 3
        word = "brute"
        
        assert util.is_char_first_occurance(word, index) == True
        
    def test_charHasOccuredBefore_assertFalse(self):
        index = 3
        word = "bleed"
        
        assert util.is_char_first_occurance(word, index) == False
        
    def test_charOccursAfter_assertTrue(self):
        index = 1
        word = "mimic"
        
        assert util.is_char_first_occurance(word, index) == True