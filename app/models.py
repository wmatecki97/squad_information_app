from typing import Optional
from pydantic import BaseModel


# For /teams endpoint
class ApiTeam(BaseModel):
    id: int
    name: str

class TeamSearchResponse(BaseModel):
    team: ApiTeam

# For /players/squads endpoint
class PlayerInSquad(BaseModel):
    id: int
    name: str
    position: str

# For /players endpoint
class BirthInfo(BaseModel):
    date: Optional[str] = None
    place: Optional[str] = None
    country: Optional[str] = None

class PlayerDetail(BaseModel):
    id: int
    firstname: str
    lastname: str
    birth: BirthInfo