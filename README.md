# RAG Gateway Service

A modular RAG (Retrieval-Augmented Generation) gateway system that routes queries to topic-specific agents.

## Features

- Topic-based routing to specialized RAG agents
- YAML-based configuration
- Async HTTP client for agent communication
- Docker support for easy deployment
- Mock agent services for testing
- OpenAPI documentation
- Convenient scripts for running tests and starting the service

## Project Structure

```
rag-gateway/
├── app/
│   ├── main.py                # FastAPI entrypoint
│   ├── router.py              # /query endpoint
│   ├── config.py              # YAML config loader
│   ├── schema.py              # Request/response models
│   ├── client.py              # HTTP client to call agents
│   └── utils.py               # Helper functions
├── config.yaml                # Routing config
├── tests/
│   └── test_routing.py        # Unit + integration tests
├── scripts/
│   ├── start.sh              # Script to start the service
│   └── test.sh               # Script to run tests
├── Dockerfile                 # For containerizing the gateway
├── docker-compose.yml         # For local testing with mock agents
├── requirements.txt
└── README.md
```

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   ./scripts/test.sh
   ```

4. Start the services using Docker Compose:
   ```bash
   ./scripts/start.sh
   ```

## API Usage

### Query Endpoint

Send a POST request to `/api/v1/query` with the following JSON payload:

```json
{
  "topic": "password_reset",
  "message": "How do I reset my password?"
}
```

The gateway will route the query to the appropriate agent based on the topic and return the response.

## Configuration

The routing configuration is defined in `config.yaml`:

```yaml
topics:
  password_reset:
    route: http://agent-password-reset:8001/query
  billing:
    route: http://agent-billing:8002/query
default_agent: http://agent-fallback:8003/query
```

## Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Testing

Run the test suite with coverage:

```bash
./scripts/test.sh
```

This will:
- Create a virtual environment if it doesn't exist
- Install dependencies if needed
- Run the test suite with coverage reporting
- Show which lines of code are not covered by tests

## Docker Support

Build and run the gateway:

```bash
docker build -t rag-gateway .
docker run -p 8000:8000 rag-gateway
```

Or use the provided script to run the complete system:

```bash
./scripts/start.sh
```

This will:
- Check if Docker is running
- Build and start all services
- Verify that services are running correctly
- Display helpful information about accessing the service

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 