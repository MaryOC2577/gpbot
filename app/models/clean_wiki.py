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
        raw_html = response["parse"]["text"]["*"]
        document = html.document_fromstring(raw_html)
        first_p = document.xpath("//p")[0]
        intro_text = first_p.text_content()
        if intro_text.isspace():
            return "Désolé GrandPy ne sais pas lire dans les pensées et n'as pas trouvé d'information concernant ce lieu. Veuillez reformuler votre demande."
        else:
            return intro_text
