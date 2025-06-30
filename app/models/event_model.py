from typing import List, Optional, Dict, Any

from pydantic import BaseModel, HttpUrl, Field



class LocationDetails(BaseModel):
    address: Optional[str] = None
    city: str
    country: Optional[str] = None

class Speaker(BaseModel):
    name: str
    title: Optional[str] = None
    organization: Optional[str] = None

class Organizer(BaseModel):
    name: str
    website: Optional[str] = None
    contactEmail: Optional[str] = None

class EventInfo(BaseModel):
    event_name: str = Field(..., alias="Event Name")
    event_type: str = Field(..., alias="Event Type")
    date_start: str = Field(..., alias="Date Start")
    date_end: str = Field(..., alias="Date End")
    time: str = Field(..., alias="Time")
    location_type: str = Field(..., alias="Location Type")
    location_details: LocationDetails = Field(..., alias="Location Details")
    online_link: Optional[str] = Field(None, alias="Online Link")
    description: str = Field(..., alias="Description")
    target_audience: str = Field(..., alias="Target Audience")
    speakers: List[Speaker] = Field(default_factory=list, alias="Speakers")
    registration_status: str = Field(..., alias="Registration Status")
    organizer: Organizer = Field(..., alias="Organizer")
    source_url: HttpUrl = Field(..., alias="Source URL")
    notes: Optional[str] = Field(None, alias="Notes")

class ResearchState(BaseModel):
    city: str
    topic: str
    events: List[EventInfo] = []
    search_results: List[Dict[str, Any]] = []
