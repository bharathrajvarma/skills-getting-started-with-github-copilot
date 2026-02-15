import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    test_email = "testuser@mergington.edu"
    # Get an activity name
    activities_resp = client.get("/activities")
    assert activities_resp.status_code == 200
    activities = activities_resp.json()
    activity_name = next(iter(activities.keys()))
    # Sign up
    signup_resp = client.post(f"/activities/{activity_name}/signup?email={test_email}")
    assert signup_resp.status_code in (200, 400)  # 400 if already signed up
    # Unregister
    unregister_resp = client.post(f"/activities/{activity_name}/unregister?email={test_email}")
    assert unregister_resp.status_code in (200, 400)  # 400 if not signed up
