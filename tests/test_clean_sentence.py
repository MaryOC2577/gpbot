"""Test sentence module."""

import pytest
from app.models.clean_sentence import Parser


class TestSentence:
    def test_is_stting(sentence):
        """Test if object is a string."""
        sentence = "test phrase contenant plusieurs mots"
        list_sentence = Parser()
        assert isinstance(list_sentence.clear_sentence(sentence), str) == True

    # --- A supprimer
    # def test_is_empty(sentence):
    #     """Error if list is empty."""
    #     sentence = "liste non vide"
    #     list_sentence = Parser()
    #     assert list_sentence.clear_sentence(sentence)

    # def test_is_string(sentence):
    #     """Test if elements are strings."""
    #     sentence = "123"
    #     list_sentence = Parser()
    #     for words in list_sentence.clear_sentence(sentence):
    #         assert isinstance(words, str) == True
    # ---

    def test_is_lower(sentence):
        """Test if sentence is in lower case."""
        sentence = "MOTS EN MAJUSCULES"
        clean_sentence = Parser()
        for words in clean_sentence.clear_sentence(sentence):
            assert words == words.lower()

    def test_when_empty(sentence):
        """Return a message when it's empty."""
        sentence = ""
        clean_sentence = Parser()
        assert (
            clean_sentence.clean_text(sentence)
            == "Désolé GrandPy ne sais pas lire dans les pensées et n'as pas trouvé d'information concernant ce lieu. Veuillez reformuler votre demande."
        )

    @pytest.mark.parametrize(
        "text,result",
        ("bonjour, je souhaite avoir l'adresse d'OpenClassrooms", ["OpenClassrooms"]),
    )
    def test_openclassrooms(text, result):
        sentence = Parser()
        assert eval(sentence.clean_text(text) == result)
