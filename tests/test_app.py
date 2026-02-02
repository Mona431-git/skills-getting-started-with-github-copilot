import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Debate Team" in data
    assert isinstance(data["Chess Club"]["participants"], list)

def test_signup_for_activity():
    # Test successful signup
    response = client.post("/activities/Chess Club/signup", params={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Signed up test@example.com for Chess Club"}

    # Verify the participant was added
    response = client.get("/activities")
    data = response.json()
    assert "test@example.com" in data["Chess Club"]["participants"]

def test_signup_activity_not_found():
    response = client.post("/activities/Nonexistent Activity/signup", params={"email": "test@example.com"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}

def test_signup_already_signed_up():
    # First signup
    client.post("/activities/Debate Team/signup", params={"email": "duplicate@example.com"})
    # Second signup should fail
    response = client.post("/activities/Debate Team/signup", params={"email": "duplicate@example.com"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up for this activity"}