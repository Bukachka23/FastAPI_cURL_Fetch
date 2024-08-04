from enum import Enum

from pydantic import BaseModel, Field


class StartEnum(str, Enum):
    fetch = "fetch"
    curl = "curl"


class TargetEnum(str, Enum):
    requests = "requests"
    https = "https"


class RequestsData(BaseModel):
    request_type: StartEnum = Field(..., description="Option fetch or curl")
    target: TargetEnum = Field(..., description="Option requests or httpx")
    data_str: str = Field(..., description="String to the enter")
