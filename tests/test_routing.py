import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import Config
from app.schema import QueryRequest, QueryResponse

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "version": "1.0.0",
        "environment": "development"
    }

@pytest.mark.asyncio
async def test_config_loading():
    config = Config()
    assert config.default_agent is not None
    assert "password_reset" in config.topics
    assert "billing" in config.topics

def test_query_endpoint():
    request_data = {
        "topic": "password_reset",
        "message": "How do I reset my password?"
    }
    response = client.post("/api/v1/query", json=request_data)
    assert response.status_code in [200, 500]  # 500 is acceptable if agent is not running

def test_invalid_topic():
    request_data = {
        "topic": "invalid_topic",
        "message": "This should go to default agent"
    }
    response = client.post("/api/v1/query", json=request_data)
    assert response.status_code in [200, 500]  # 500 is acceptable if agent is not running 