def test_remove_participant_from_activity_success(client):
    # Arrange
    activity_name = "Basketball Team"
    email = "alex@mergington.edu"
    remove_path = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(remove_path, params={"email": email})
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity_name}"
    assert email not in participants


def test_remove_participant_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    remove_path = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(remove_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_participant_returns_404_when_email_not_enrolled(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not-enrolled@mergington.edu"
    remove_path = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(remove_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"