"""Clean a sentence."""

class CleanSentence:

    def clear_sentence(sentence):
        """Clear a sentence into a list."""
        result = str(sentence).lower().replace(",", ";", ".").split()
        # ''.join( c for c in line if  c not in '?:!/;' )
        return result
