import requests

from lxml import html

# import wikipedia


class WikiInfo:
    def clean_wiki(self, location):
        # intro_text = wikipedia.summary(location)
        # print(intro_text)
        # return intro_text

        response = requests.get(
            "https://fr.wikipedia.org/w/api.php",
            params={
                "action": "parse",
                "page": location,
                "format": "json",
            },
        ).json()

        # print(response)
        raw_html = response["parse"]["text"]["*"]
        document = html.document_fromstring(raw_html)
        first_p = document.xpath("//p")[0]
        intro_text = first_p.text_content()
        if intro_text.isspace():
            return "Désolé GrandPy ne sais pas lire dans les pensées et n'as pas trouvé d'information concernant ce lieu. Veuillez reformuler votre demande."
        else:
            return intro_text
