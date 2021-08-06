"""Test sentence module."""

from app.models.clean_sentence import CleanSentence


class TestSentence:
    def test_is_list(sentence):  # Pourquoi vouloir une liste ? Quel bénéfice dans l'utilisation du parser ? A priori, on préfère un string - pourquoi ?
        """Test if object is a list."""
        sentence = "test phrase contenant plusieurs mots"
        list_sentence = CleanSentence()
        assert isinstance(list_sentence.clear_sentence(sentence), list) == True

    def test_is_empty(sentence):  # pourquoi vérifier que ce n'est pas vide ?
        """Error if list is empty."""
        sentence = "liste non vide"  # par exemple, ceci n'a pas d'intérêt en terme de recherche, et devrait dans l'idéal, être complètement nettoyé :O
        list_sentence = CleanSentence()  # ceci n'est pas une liste
        assert list_sentence.clear_sentence(sentence)

    def test_is_string(sentence):  # si tu simplifie le retour en tant que string, plus besoin de cette méthode
        """Test if elements are strings."""
        sentence = "123"
        list_sentence = CleanSentence()
        for words in list_sentence.clear_sentence(sentence):
            assert isinstance(words, str) == True

    def test_is_lower(sentence):  # pourquoi pas
        """Test if sentence is in lower case."""
        sentence = "MOTS EN MAJUSCULES"
        list_sentence = CleanSentence()
        for words in list_sentence.clear_sentence(sentence):
            assert words == words.lower()
            
    # il manque pour moi:
    #  -- des tests qui vérifie le retour d'une phrase ("bonjour, je souhaite avoir l'adresse d'OpenClassrooms" ---> "openclassrooms"
    # pour ça, utiliser pytests.mark.parametrize j'aimerai bien, car cela te permettra d'effectuer un grand nombre de tests de c genre rapidement
    # -- un test qui vérifie ce qui se passe quand c'est vide
    # -- et voila pour l'instant

    # tester si la liste contient des stops words
    # def test_is_stop_words(sentence):
    #     sentence = "cette phrase contient divers euh stop words"
    #     list_sentence = CleanSentence()
    #     assert list_sentence.clear_sentence(
    #         sentence
    #     ) == list_sentence.delete_stop_words(list_sentence.clear_sentence(sentence))
