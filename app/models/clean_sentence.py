"""Clean a sentence."""

from app.models.stop_words import list_words

class CleanSentence:

    def clear_sentence(sentence):
        """Clear a sentence into a list."""
        result = str(sentence).lower().split()
        # ''.join( c for c in line if  c not in '?:!/;' )
        return result

    def delete_stop_words(list_sentence):
        """Delete stop_words in a list."""
        for word in list_sentence:
            if word in list_words:
                del list_sentence[list_sentence.index(word)]
        return list_sentence