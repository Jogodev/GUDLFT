import server

class TestMaxPlaces:
    
    def test_can_purchase_12_places_max_valid(self, client):
        club = server.clubs[2]
        competition = server.competitions[0]
        response = client.post("/purchasePlaces", data={"club": club['name'], "competition": competition['name'], 'places': 12})
        
        assert response.status_code == 200
        assert b"Great-booking complete!" in response.data
        
    def test_can_purchase_12_places_max_invalid(self, client):
        club = server.clubs[2]
        competition = server.competitions[0]
        response = client.post("/purchasePlaces", data={"club": club['name'], "competition": competition['name'], 'places': 13})
        
        assert response.status_code == 200
        assert b"You able to book 12 places no more!" in response.data
        