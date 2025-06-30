class ResearchPromo:

    EVENT_ANALYSIS_SYSTEM = """
        You are analyzing events, conferences, workshops, and meetups.
        Focus on extracting structured and factual information about each event.

        Pay special attention to:
        - Event name and type (e.g., conference, webinar, workshop)
        - Dates and times
        - Location (physical or online), with city and country
        - Organizer’s name
        - Source URL

        Ensure all output is complete and well-structured for use in an event aggregation system.
        Respond only with a list of event entries using the format provided.
        """

    @staticmethod
    def event_analysis_content(content: str, source_url: str) -> str:
        return f"""
        Extract events from the following website content:

        \"\"\"
        {content}
        \"\"\"

        For each event you find, return the following structured information in plain text format:

        - event_name: Full official name of the event.
        - event_type: (e.g., Conference, Workshop, Webinar, Meetup, Festival, Expo, Seminar)
        - date_start: YYYY-MM-DD
        - date_end: YYYY-MM-DD
        - time: Time range or start time, including timezone if available.
        - location_type: "Physical", "Online", or "Hybrid"
        - address: Full venue address (if applicable, otherwise null)
        - city: City where the event is based or targeted
        - country: Country (if physical, otherwise null)
        - online_link: Link to attend (if applicable, otherwise null)
        - description: Concise 1–3 sentence factual summary
        - target_audience: Who the event is for (e.g., "AI professionals", "students")
        - speakers:
            - name: Speaker name
            title: Optional job title
            organization: Optional affiliation
        - registration_status: e.g., "Open", "Closed", "RSVP Required", "Sold Out"
        - organizer:
            name: Organizer’s name
            website: Organizer’s website (optional)
            contactEmail: Contact email (optional)
        - source_url: {source_url}
        - notes: Any other info, or null
        """
