import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "New task",
        "description": "Task description"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)

    assert response.status_code == 200
    assert "message" in response.json()
    assert "id" in response.json()

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")

    assert response.status_code == 200
    assert "tasks" in response.json()
    assert "total_tasks" in response.json()

def test_get_tasks():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")

        assert response.status_code == 200
        assert task_id == response.json()["id"]
    
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "test description",
            "title": "test title"
        }

        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        
        assert response.status_code == 200
        assert "message" in response.json()

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")

        assert response.status_code == 200
        assert response.json()["title"] == "test title"
        assert response.json()["description"] == "test description"
        assert response.json()["completed"] == True
