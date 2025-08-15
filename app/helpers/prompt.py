class ResearchPromo:
    def event_analysis_system(self, topic: str, city: str, start_date: str, end_date: str) -> str:
        return f"""You are an expert event analyst specializing in extracting comprehensive information about events, conferences, workshops, and meetups.

        Your task is to analyze web content and extract ALL relevant events that match the specified criteria.

        **FILTERING CRITERIA:**
        - Location/City: {city} (exact match, case-insensitive)
        - Topic: {topic} (related topics and synonyms are acceptable)
        - Date Range: {start_date} to {end_date} (inclusive)

        **ANALYSIS REQUIREMENTS:**
        1. Extract EVERY event that matches the criteria - don't miss any
        2. Be thorough in identifying event-related content (look for event listings, calendars, announcements)
        3. Handle various date formats (MM/DD/YYYY, DD/MM/YYYY, Month DD, YYYY, etc.)
        4. Identify both explicit and implicit event information
        5. Look for events in tables, lists, paragraphs, and embedded content
        6. Pay attention to recurring events and event series

        **EVENT TYPES TO IDENTIFY:**
        - Conferences, Workshops, Seminars
        - Meetups, Networking events
        - Webinars, Virtual events
        - Festivals, Exhibitions, Trade shows
        - Training sessions, Bootcamps
        - Hackathons, Competitions
        - Panel discussions, Talks

        **OUTPUT FORMAT:**
        Ensure all extracted information is accurate and sourced from the provided content."""

    @staticmethod
    def event_analysis_content(content: str, source_url: str, city: str, topic: str, start_date: str, end_date: str) -> str:
        """Enhanced content analysis prompt with better extraction instructions."""
        return f"""ANALYZE the following website content and extract ALL events that match these criteria:

        **MANDATORY FILTERS:**
        ✓ City: {city} (exact match required)
        ✓ Topic: {topic} (must be related to this topic or its synonyms)
        ✓ Date: Between {start_date} and {end_date} (inclusive)

        **CONTENT TO ANALYZE:**
        \"\"\"
        {content}
        \"\"\"

        **EXTRACTION INSTRUCTIONS:**
        1. Scan the ENTIRE content thoroughly - don't miss any events
        2. Look for event information in all formats: tables, lists, paragraphs, calendars
        3. Extract events from announcements, schedules, and upcoming events sections
        4. Handle various date formats and convert to YYYY-MM-DD
        5. Identify both single-day and multi-day events
        6. Look for recurring events within the date range


          For each valid event you find, return the following structured information in plain text format:

            - event_name: Full official name of the event.
            -event_type: (e.g., Conference, Workshop, Webinar, Meetup, Festival, Expo, Seminar)
            -start_date: YYYY-MM-DD
            -end_date: YYYY-MM-DD
            -time: Time range or start time, including timezone if available.
            -location_type: "Physical", "Online", or "Hybrid"
            -address: Full venue address (if applicable, otherwise null)
            -city: Must be {city}
            -country: Country (if physical, otherwise null)
            -online_link: Link to attend (if applicable, otherwise null)
            -description: Concise 1–3 sentence factual summary
            -target_audience: Who the event is for (e.g., "AI professionals", "students")
            -registration_status: e.g., "Open", "Closed", "RSVP Required", "Sold Out"
            -organizer:
                name: Organizer’s name
                website: Organizer’s website (optional)
                contact_email: Contact email (optional)
            -source_url: {source_url}

        **IMPORTANT NOTES:**
        - Return ONLY valid JSON format
        - If no events match criteria, return: []
        - Ensure all dates are in YYYY-MM-DD format
        - Be thorough - extract ALL matching events
        - Use "null" for missing information, not empty strings
        - Validate that city and topic match exactly"""
