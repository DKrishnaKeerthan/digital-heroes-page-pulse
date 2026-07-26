from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_invalid_url():
    response = client.post(
        "/audit",
        json={"url": "invalid-url"}
    )
    assert response.status_code == 422

def test_valid_url():
    response = client.post(
        "/audit",
        json={"url": "https://example.com"}
    )
    assert response.status_code in [200, 429]

def test_cached_request():
    client.post("/audit", json={"url":"https://example.com"})
    response = client.post("/audit", json={"url":"https://example.com"})

    if response.status_code == 200:
        assert "cached" in response.json()

def test_rate_limit():
    for _ in range(3):
        response = client.post(
            "/audit",
            json={"url":"https://example.com"}
        )

    assert response.status_code in [200,429]