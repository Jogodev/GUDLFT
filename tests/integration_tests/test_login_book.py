import server

class TestLoginBook:
    def test_login_book(self, client):
        club = server.clubs[2]
        competition = server.competitions[2]
        login_user = client.post("/showSummary", data={"email": club['email']})
        
        assert club['email'] in login_user.data.decode()
        assert login_user.status_code == 200
        
        response = client.post("/purchasePlaces", data={"club": club['name'], "competition": competition['name'], 'places': 13})
        
        assert b"You able to book 12 places no more!" in response.data
        assert response.status_code == 200
        
        response = client.post("/purchasePlaces", data={"club": club['name'], "competition": competition['name'], 'places': 7})
        
        assert response.status_code == 200
        assert b"Great-booking complete!" in response.data