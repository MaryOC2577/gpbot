import pytest
from app.models.clean_sentence import CleanSentence

# tester si la phrase est une liste 
def split_list_sentence(self):
    sentence = "une phrase longue pour tester"
    result = CleanSentence().split_sentence(sentence)
    return result

def test_split_list_sentence():
    assert isinstance(split_list_sentence(), list) == True

# tester si la liste contient des string

# tester si la liste contient des stops words
#def test_cleanup_sentence_nostopwords(sentence):

# tester si la liste contient un lieu
