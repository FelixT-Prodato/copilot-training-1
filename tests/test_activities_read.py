def test_get_activities_returns_activity_dictionary(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert expected_activity in payload


def test_get_activities_contains_expected_activity_fields(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    activity = response.json()["Chess Club"]
    assert expected_fields.issubset(activity.keys())
