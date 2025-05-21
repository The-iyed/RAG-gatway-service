from fastapi import APIRouter, HTTPException, Depends
from .schema import QueryRequest, QueryResponse
from .config import Config
from .client import AgentClient

router = APIRouter()

async def get_agent_client():
    client = AgentClient()
    try:
        yield client
    finally:
        await client.close()

@router.post("/query", response_model=QueryResponse)
async def query(
    request: QueryRequest,
    config: Config = Depends(lambda: Config()),
    client: AgentClient = Depends(get_agent_client)
) -> QueryResponse:
    """Route a query to the appropriate agent based on the topic."""
    try:
        agent_url = config.get_agent_url(request.topic)
        response = await client.query_agent(agent_url, request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 