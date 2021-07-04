"""Clean a sentence."""

import json


class CleanSentence:
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
        list_words = self.load_stop_words()
        for word in list_sentence:
            if word in list_words:
                del list_sentence[list_sentence.index(word)]
        return list_sentence

    def clean_sentence(self, sentence):
        return self.delete_stop_words(self.clear_sentence(sentence))
