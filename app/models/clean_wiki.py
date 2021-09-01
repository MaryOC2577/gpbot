import requests

from lxml import html


class WikiAPI:
    def find_page(self, location):

        data = requests.get(
            "https://fr.wikipedia.org/w/api.php",
            params={
                "action": "opensearch",
                "search": location,
                "format": "json",
                "limit": 1,
                "namespace": 0,
            },
        ).json()
        url = "".join(data[3])
        return url

    def get_text(self, location):

        wiki_url = self.find_page(location)
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

        if response["title"] == "Not found.":
            intro_text = (
                "Désolé GrandPy ne peut pas trouver un lieu" " qui n'existe pas."
            )
        else:
            intro_text = response["extract"]

        if not intro_text.replace(" ", ""):
            return (
                "Désolé GrandPy ne sais pas lire dans "
                "les pensées et n'as pas trouvé d'information concernant"
                " ce lieu. Veuillez reformuler votre demande."
            )
        else:
            wiki_info = [intro_text, wiki_url]
            return wiki_info
