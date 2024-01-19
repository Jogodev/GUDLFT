import server


class TestAllowedPoints:
    def test_allowed_points_not_enough(self, client):
        club = server.clubs[1]
        competition = server.competitions[1]
        response = client.post(
            "/purchasePlaces",
            data={
                "club": club["name"],
                "competition": competition["name"],
                "places": 10,
            },
        )

        assert b"Not enough points" in response.data
        assert response.status_code == 200
        
    def test_allowed_points_enough(self, client):
        club = server.clubs[1]
        competition = server.competitions[1]
        response = client.post(
            "/purchasePlaces",
            data={
                "club": club["name"],
                "competition": competition["name"],
                "places": 5,
            },
        )

        assert b"Great-booking complete!" in response.data
        assert response.status_code == 200
