"""Clean a sentence."""

import json


class Parser:
    def load_stop_words(self):
        with open("app/data/stopwords.json", "r") as json_data:
            stop_words = json.load(json_data)
        return stop_words

    def clear_sentence(self, sentence):
        """Clear a sentence into a list."""
        result = str(sentence).lower().split()
        return result

    def delete_stop_words(self, list_sentence):
        """Delete stop_words in a list."""
        stop_words = self.load_stop_words()["stop words"]
        stop_chars = self.load_stop_words()["stop chars"]
        for element in stop_words:
            for word in list_sentence:
                for letter in word:
                    if letter in stop_chars:
                        word.replace(letter, " ")
                if word == element:
                    del list_sentence[list_sentence.index(word)]

        return list_sentence

    def clean_text(self, sentence):
        if sentence == "":
            err_msg = "Désolé GrandPy ne sais pas lire dans les pensées et n'as pas trouvé d'information concernant ce lieu. Veuillez reformuler votre demande."
            return err_msg
        else:
            return " ".join(self.delete_stop_words(self.clear_sentence(sentence)))
