import requests

from app.models.gps_coordinates import HereAPI


class FakeResponse:
    def json(self):
        # return {
        #     "coords": {"lat": 48.85717, "lng": 2.3414},
        #     "adress": "Paris, Île-de-France, France",
        # }
        return {
            "items": [
                {
                    "position": {"lat": 48.85717, "lng": 2.3414},
                    2: "",
                    "title": "Paris, Île-de-France, France",
                }
            ]
        }


def test_get_coords(monkeypatch):
    def fake_get(*args, **kwargs):
        return FakeResponse()

    api = HereAPI()
    location = "paris"
    monkeypatch.setattr(requests, "get", fake_get)
    result = {
        "coords": {"lat": 48.85717, "lng": 2.3414},
        "adress": "Paris, Île-de-France, France",
    }
    assert api.find_coordinates(location) == result
