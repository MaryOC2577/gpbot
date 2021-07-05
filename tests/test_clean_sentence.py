"""Test sentence module."""

from app.models.clean_sentence import CleanSentence


class TestSentence:
    def test_is_list(sentence):
        """Test if object is a list."""
        sentence = "test phrase contenant plusieurs mots"
        list_sentence = CleanSentence()
        assert isinstance(list_sentence.clear_sentence(sentence), list) == True

    def test_is_empty(sentence):
        """Error if list is empty."""
        sentence = "liste non vide"
        list_sentence = CleanSentence()
        assert list_sentence.clear_sentence(sentence)

    def test_is_string(sentence):
        """Test if elements are strings."""
        sentence = "123"
        list_sentence = CleanSentence()
        for words in list_sentence.clear_sentence(sentence):
            assert isinstance(words, str) == True

    def test_is_lower(sentence):
        """Test if sentence is in lower case."""
        sentence = "MOTS EN MAJUSCULES"
        list_sentence = CleanSentence()
        for words in list_sentence.clear_sentence(sentence):
            assert words == words.lower()

    # tester si la liste contient des stops words
    def test_is_stop_words(sentence):
        sentence = "cette phrase contient divers euh stop words"
        list_sentence = CleanSentence()
        assert list_sentence.clear_sentence(
            sentence
        ) == list_sentence.delete_stop_words(list_sentence.clear_sentence(sentence))
