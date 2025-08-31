from pydantic import BaseModel

class IPCSingleRequest(BaseModel):
    ipc_section: str
