"""Clean a sentence."""

from app.models.stop_words import list_words


class CleanSentence:
    def clear_sentence(self, sentence):
        """Clear a sentence into a list."""
        result = str(sentence).lower().split()
        return result

    def delete_stop_words(self, list_sentence):
        """Delete stop_words in a list."""
        for word in list_sentence:
            if word in list_words:
                del list_sentence[list_sentence.index(word)]
        return list_sentence

    def clean_sentence(self, sentence):
        self.delete_stop_words(self.clear_sentence(sentence))
