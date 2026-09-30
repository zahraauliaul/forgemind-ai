from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, raise_server_exceptions=False)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["service"] == "ForgeMind AI"

def test_internal_server_error():
    from fastapi import APIRouter

    router = APIRouter()

    @router.get("/test-error")
    def test_error():
        raise RuntimeError("secret internal error")

    from app.main import app

    app.include_router(router)

    response = client.get("/test-error")

    assert response.status_code == 500

    data = response.json()

    assert data["error"] == "internal_server_error"
    assert data["message"] == "An unexpected error occurred."
    assert "secret internal error" not in response.text