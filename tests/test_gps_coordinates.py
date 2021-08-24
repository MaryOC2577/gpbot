import requests

from app.models.gps_coordinates import HereAPI


class FakeResponse:
    def json(self):
        return {
            "coords": {"lat": 48.85717, "lng": 2.3414},
            "adress": "Paris, Île-de-France, France",
        }


def test_get_coords(monkeypatch):
    def fake_get(*args, **kwargs):
        return FakeResponse()

    coords = HereAPI()
    location = "paris"
    monkeypatch.setattr(requests, "get", fake_get)
    assert coords.find_coordinates(location)
