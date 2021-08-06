import requests


class WikiResult:  # pareil que pour here
    def execute(self):
        return requests.get("https://fr.wikipedia.org/w/api.php").json()


class FakeResponse:
    def json(self):
        return "Une phrase de test."


def test_execute(monkeypatch):
    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)
    wiki = WikiResult()
    assert wiki.execute() == "Une phrase de test."  # être sure que le retour de mediawiki est bien une string direct et non un dictionnaire de données
