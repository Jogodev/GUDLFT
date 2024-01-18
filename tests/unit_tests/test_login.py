from server import showSummary, app
from flask import json

class TestLogin:
    def test_mail_invalid(self, client):
        wrong_email = "johntest@gmail.com"
        response = client.post("/showSummary", data={"email": wrong_email})
            
        assert b"Email not found." in response.data
        assert response.status_code == 200


    def test_mail_valid(self, client):
        response = client.post("/showSummary", data={"email": 'beta@gmail.com'})

        assert b'beta@gmail.com' in response.data
        assert response.status_code == 200
