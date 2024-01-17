from server import showSummary, app
from tests.conftest import client, clubs_fixtures
from flask import json


def test_mail_invalid(client):
    wrong_email = "johntest@gmail.com"
    response = client.post("/showSummary", data={"email": wrong_email})
        
    assert b"Email not found." in response.data
    assert response.status_code == 200


def test_mail_valid(client, clubs_fixtures):
    clubs = clubs_fixtures[0]
    good_email = "jotest@gmail.com"
    response = client.post("/showSummary", data={"email": good_email})

    assert good_email in clubs['email']
    assert response.status_code == 200
