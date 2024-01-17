import pytest
import server


@pytest.fixture()
def clubs_fixtures():
    data = [
        {"name": "Simply Lift", "email": "jotest@gmail.com", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
    ]
    return data


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
