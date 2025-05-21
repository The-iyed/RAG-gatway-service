from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class QueryRequest(BaseModel):
    topic: str = Field(..., description="The topic of the query")
    message: str = Field(..., description="The message to be processed")

class QueryResponse(BaseModel):
    response: str = Field(..., description="The response from the agent")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata from the agent") 