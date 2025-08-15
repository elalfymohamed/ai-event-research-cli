from typing import List, Optional, Dict, Any

from pydantic import BaseModel, HttpUrl


class LocationDetails(BaseModel):
    address: Optional[str] = None
    city: str
    country: Optional[str] = None

class Organizer(BaseModel):
    name:  Optional[str] = None
    website: Optional[str] = None
    contactEmail: Optional[str] = None

class EventInfo(BaseModel):
    event_name: str
    event_type: str
    start_date: str
    end_date: str
    time: Optional[str] = None
    location_type: Optional[str] = None
    location_details: LocationDetails
    online_link: Optional[str] = None
    description: Optional[str] = None
    target_audience: Optional[str] = None
    registration_status: Optional[str] = None
    organizer: Organizer
    source_url: HttpUrl

class ResearchState(BaseModel):
    city: str
    topic: str
    events: List[Dict[str, Any]]  = []
    search_results: List[Dict[str, Any]] = []
    urls:  List[HttpUrl] = []
