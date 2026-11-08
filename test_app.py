from app import app, add


def test_add_function():
    assert add(2, 3) == 6
    assert add(-1, 1) == 0


def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from the CI/CD pipeline!"


def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_route():
    client = app.test_client()
    response = client.get("/add/4/6")
    assert response.status_code == 200
    assert response.get_json()["result"] == 10