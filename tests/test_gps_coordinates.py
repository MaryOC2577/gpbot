import requests


class GpsCoords:  # ne pas utiliser ce code ;) le but est de tester la classe de ton code source !
    def execute(self):
        return requests.get("https://geocode.search.hereapi.com/v1/geocode").json()


class FakeResponse:
    def json(self):
        return {"lat": 48.87695, "lng": 2.29362}


def test_execute(monkeypatch):
    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)
    coords = GpsCoords()
    assert coords.execute() == {"lat": 48.87695, "lng": 2.29362}  # il me semble que tu traites aussi l'adresse donc ajoute là ici aussi
