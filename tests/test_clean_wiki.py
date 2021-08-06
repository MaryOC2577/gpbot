import requests


class WikiResult:
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
    assert wiki.execute() == "Une phrase de test."
