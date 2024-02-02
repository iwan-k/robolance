from pydantic import BaseModel


class Robolancer(BaseModel):
    id: int
    title: str
    description: str
    thumbnail: str
    location: str
    hourly_rate: int
