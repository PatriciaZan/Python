from typing import Literal

from pydantic import BaseModel

# espera
class LoginRequest(BaseModel):
    username: str
    password: str

# vai entregar
class LoginResponse(BaseModel):
    authenticated: bool
    userName: str
    userPermission: Literal["intern", "restricted", "public"]
    access_token: str