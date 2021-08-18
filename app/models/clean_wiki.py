import requests

from lxml import html


class WikiAPI:
    def find_wiki_text(self, location):

        response = requests.get(
            "https://fr.wikipedia.org/w/api.php",
            params={
                "action": "opensearch",
                "search": location,
                "format": "json",
                "limit": 1,
                "namespace": 0,
            },
        ).json()
        url = "".join(response[3])
        return url

    def get_wiki_text(self, location):

        wiki_url = self.find_wiki_text(location)
        json_url = (
            "https://fr.wikipedia.org/api/rest_v1/page/summary/"
            + location.replace(" ", "_")
        )
        response = requests.get(
            json_url,
            params={
                "action": "opensearch",
                "format": "json",
            },
        ).json()

        intro_text = response["extract"]

        if intro_text.isspace():
            return "Désolé GrandPy ne sais pas lire dans les pensées et n'as pas trouvé d'information concernant ce lieu. Veuillez reformuler votre demande."
        else:
            wiki_info = [intro_text, wiki_url]
            return wiki_info
