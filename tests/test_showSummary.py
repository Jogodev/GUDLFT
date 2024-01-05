from server import showSummary

def test_showSummary(client):
    wrong_mail = "jotest@gmail.com"
    response = client.post('/showSummary')