from typing import List, Optional, Dict, Any

from pydantic import BaseModel, HttpUrl


class LocationDetails(BaseModel):
    address: Optional[str] = None
    city: str
    country: Optional[str] = None

class Organizer(BaseModel):
    name: str
    website: Optional[str] = None
    contactEmail: Optional[str] = None

class EventInfo(BaseModel):
    event_name: str
    event_type: str
    date_start: str
    date_end: str
    time: str
    location_type: str
    location_details: LocationDetails
    online_link: Optional[str] = None
    description: str
    target_audience: str
    registration_status: str
    organizer: Organizer
    source_url: HttpUrl

class ResearchState(BaseModel):
    city: str
    topic: str
    events: List[EventInfo] = []
    search_results: List[Dict[str, Any]] = []
    urls:  List[str] = []
