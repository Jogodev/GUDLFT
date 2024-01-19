import server


class TestBookInPastCompetition:
    def test_book_in_past_competition(self, client):
        club = server.clubs[0]
        competition = server.competitions[0]
        response = client.post(
            "/purchasePlaces",
            data={
                "club": club["name"],
                "competition": competition["name"],
                "places": 5,
            },
        )
        print(response.data)
        assert response.status_code == 200
        assert b"This competition is past!" in response.data

    def test_book_in_future_competition(self, client):
        club = server.clubs[0]
        competition = server.competitions[2]
        response = client.post(
            "/purchasePlaces",
            data={
                "club": club["name"],
                "competition": competition["name"],
                "places": 5,
            },
        )

        assert response.status_code == 200
        assert b"Great-booking complete!" in response.data
