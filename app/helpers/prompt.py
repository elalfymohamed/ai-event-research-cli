
class ResearchPromo:
    def EVENT_ANALYSIS_SYSTEM(self, topic: str, city: str, start_date: str, end_date: str) -> str:
        return f"""You are analyzing events, conferences, workshops, and meetups.
        Focus on extracting structured and factual information about each event.

        Pay special attention to:
        - Location/city: {city}
        - Topic: {topic}
        - Date: between {start_date} and {end_date}
        - Event name and type (e.g., conference, webinar, workshop)
        - Dates and times
        - Location (physical or online), with city and country
        - Organizer’s name
        - Source URL

        Ensure all output is complete and well-structured for use in an event aggregation system.
        Respond only with a list of event entries using the format provided.
        """

    @staticmethod
    def event_analysis_content(content: str, source_url: str, city: str, topic: str, start_date:str, end_date:str) -> str:
        return f"""Extract only the events from the following website content that match **both** of the following criteria:

            1. City must be **{city}** (ignore other cities)
            2. Topic must be **{topic}** (ignore unrelated topics)
            3. Date must be between **{start_date}** and **{end_date}** (ignore other Date)

            \"\"\"
            {content}
            \"\"\"

            Ignore general listings or summaries not directly related to this city and topic.

            For each valid event you find, return the following structured information in plain text format:

            - event_name: Full official name of the event.
            - event_type: (e.g., Conference, Workshop, Webinar, Meetup, Festival, Expo, Seminar)
            - date_start: YYYY-MM-DD
            - date_end: YYYY-MM-DD
            - time: Time range or start time, including timezone if available.
            - location_type: "Physical", "Online", or "Hybrid"
            - address: Full venue address (if applicable, otherwise null)
            - city: Must be {city}
            - country: Country (if physical, otherwise null)
            - online_link: Link to attend (if applicable, otherwise null)
            - description: Concise 1–3 sentence factual summary
            - target_audience: Who the event is for (e.g., "AI professionals", "students")
            - registration_status: e.g., "Open", "Closed", "RSVP Required", "Sold Out"
            - organizer:
                name: Organizer’s name
                website: Organizer’s website (optional)
                contact_email: Contact email (optional)
            - source_url: {source_url}
            """
