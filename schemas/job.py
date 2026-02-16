from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

# To jest to, co bot MUSI wysłać, żeby oferta wpadła do systemu
class JobBase(BaseModel):
    external_id: str
    title: str
    company: Optional[str] = None
    location: str
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    currency: str = "NOK"
    tags: List[str] = []  # Tutaj wpadnie: CNC, Heidenhain, T8, UDT itp.
    url: str

# To system nam pokaże, jak już zapisze ofertę (doda ID i datę)
class JobRead(JobBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True