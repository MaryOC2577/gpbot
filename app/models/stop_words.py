"""Stop words."""

import json

class StopWords:

    def load_stop_words(self):
        with open('app/models/stopwords.json') as json_data:
            stop_words = json.dump(json_data)