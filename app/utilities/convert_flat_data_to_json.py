from typing import NamedTuple

class LocationDetails(NamedTuple):
    address: str
    city: str
    country: str

class Organizer(NamedTuple):
    name: str
    website: str
    contactEmail: str

class HttpUrl(str):
    pass

def convert_flat_data_to_json(data):
    events = []
    event = {}

    for key, value in data:
        if key == 'event_name' and event:
            events.append(event)
            event = {}

        if isinstance(value, LocationDetails):
            value = {
                "address": value.address,
                "city": value.city.title() if value.city else None,
                "country": value.country
            }
        elif isinstance(value, Organizer):
            value = {
                "name": value.name,
                "website": value.website,
                "contact_email": value.contactEmail
            }
        elif isinstance(value, HttpUrl):
            value = str(value)

        event[key] = value

    if event:
        events.append(event)

    return events
