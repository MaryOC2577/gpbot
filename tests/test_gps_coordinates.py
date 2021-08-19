import requests

from app.models.gps_coordinates import HereAPI


class FakeResponse:
    def json(self):
        return {
            "lat": 48.87695,
            "lng": 2.3414,
            "adress": "Paris, Île-de-France, France",
        }


def test_execute(monkeypatch):
    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)
    coords = HereAPI()
    assert coords.find_coordinates("paris") == test_execute()
