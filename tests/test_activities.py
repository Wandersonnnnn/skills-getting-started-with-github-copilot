def test_get_activities_returns_expected_dictionary(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data