import pytest
import server


@pytest.fixture(scope="function", autouse=True)
def clubs_fixtures(monkeypatch):
    data = [
        {"name": "Club Alpha", "email": "alpha@gmail.com", "points": "5"},
        {"name": "Club Beta", "email": "beta@gmail.com", "points": "7"},
        {"name": "Club Delta", "email": "delta@gmail.co.uk", "points": "14"},
    ]
    monkeypatch.setattr("server.clubs", data)


@pytest.fixture(scope="function", autouse=True)
def competitions_fixtures(monkeypatch):
    data = [
        {
            "name": "Summer Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "22",
        },
        {
            "name": "Arnold Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13",
        },
        {"name": "Strong Event", "date": "2024-10-22 13:30:00", "numberOfPlaces": "30"},
    ]
    monkeypatch.setattr("server.competitions", data)


@pytest.fixture()
def app():
    app = server.app
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
