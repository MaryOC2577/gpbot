"""Test sentence module."""

from app.models.clean_sentence import CleanSentence

class TestSentence:

    def test_is_list(sentence):
        """Test if object is a list."""
        sentence = "test phrase contenant plusieurs mots"
        list_sentence = CleanSentence.clear_sentence(sentence)
        assert isinstance(list_sentence, list) == True

    def test_is_empty(sentence):
        """Error if list is empty."""
        sentence = "liste non vide"
        list_sentence = CleanSentence.clear_sentence(sentence)
        assert list_sentence

    def test_is_string(sentence):
        """Test if elements are strings."""
        sentence = "123"
        list_sentence = CleanSentence.clear_sentence(sentence)
        for words in list_sentence:
            assert isinstance(words, str) == True

    def test_is_lower(sentence):
        """Test if sentence is in lower case."""
        sentence = "MOTS EN MAJUSCULES"
        list_sentence = CleanSentence.clear_sentence(sentence)
        for words in list_sentence:
            assert words == words.lower()

    # tester si la liste contient des signes de ponctuation
    # def test_not_punctuaction_mark(sentence):
    #     sentence = "Phrase; avec des signes. de, ponctuation..."
    #     list_sentence = CleanSentence.clear_sentence(sentence)
    #     assert list_sentence == sentence.replace(";", ",", ".").split()

    # tester si la liste contient des stops words
    def test_is_stop_words(sentence):
        sentence = "cette phrase contient divers euh stop words"
        list_sentence = CleanSentence.clear_sentence(sentence)
        assert list_sentence == CleanSentence.delete_stop_words(list_sentence)