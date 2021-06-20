import pytest
from app.models.clean_sentence import CleanSentence

class TestCleanSentence:

    # tester si la phrase est une liste 
    def split_list_sentence(self):
        sentence = "absolument rendre à"
        return CleanSentence().split_sentence(sentence)
     
    def test_split_list_sentence(self):
        assert isinstance(self.split_list_sentence(), list) == True

    # tester si la liste contient des string
    def test_string_in_list(self):
        for element in self.split_list_sentence():
            assert isinstance(element, str) == True

    # tester si les mots sont en minuscules

    # tester si les mots de la liste contiennent des accents, caractères spéciaux...

    # tester si la liste ne contient pas des stops words
    def test_cleanup_sentence_nostopwords(self):
        for element in self.split_list_sentence():
            for words in CleanSentence().stop_words:
                assert element != words


