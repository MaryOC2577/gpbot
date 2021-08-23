import requests

from app.models.clean_wiki import WikiAPI


class FakeResponse:
    def json(self):
        return {"extract": "", 3: ""}


def test_wiki_if_no_result(monkeypatch):
    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)
    wiki = WikiAPI()
    assert wiki.get_text("paris").startswith("Désolé GrandPy")
