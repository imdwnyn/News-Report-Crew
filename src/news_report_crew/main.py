# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Import crew class
from news_report_crew.crew import NewsReportCrew


def run():
    """
    Entry point to run the crew
    """

    # Inputs passed into YAML placeholders like {country}
    inputs = {
        "country": "India"
    }

    try:
        # Start the crew execution
        result = NewsReportCrew().crew().kickoff(inputs=inputs)

    except Exception as e:
        # If anything fails, show readable error
        raise Exception(f"An error occurred while running the crew: {e}")