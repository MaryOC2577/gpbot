"""Test sentence module."""

import pytest
from app.models.clean_sentence import Parser


class TestSentence:
    def test_is_string(self):
        """Test if object is a string."""
        sentence = "test phrase contenant plusieurs mots"
        list_sentence = Parser()
        assert isinstance(list_sentence.clean_text(sentence), str)

    def test_is_lower(self):
        """Test if sentence is in lower case."""
        sentence = "MOTS EN MAJUSCULES"
        clean_sentence = Parser()
        for words in clean_sentence.clear_sentence(sentence):
            assert words == words.lower()

    def test_when_empty(self):
        """Return a message when it's empty."""
        sentence = ""
        clean_sentence = Parser()
        assert (
            clean_sentence.clean_text(sentence)
            == "Désolé GrandPy ne sais pas lire dans les pensées et n'as pas trouvé "
            + "d'information concernant ce lieu. Veuillez reformuler votre demande."
        )

    @pytest.mark.parametrize(
        "text,result",
        (["bonjour, je souhaite avoir l'adresse d'OpenClassrooms", "openClassrooms"],),
    )
    def test_openclassrooms(self, text, result):
        sentence = Parser()
        assert sentence.clean_text(text) == result
