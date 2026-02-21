# Import core CrewAI classes
from crewai import Agent, Crew, Process, Task

# Decorators used by CrewAI to auto-register agents, tasks, and crew
from crewai.project import CrewBase, agent, crew, task

# BaseAgent typing
from crewai.agents.agent_builder.base_agent import BaseAgent

# Typing support
from typing import List

# Pydantic for structured JSON output
from pydantic import BaseModel, Field

# Search tool from crewai-tools package (uses Serper API)
from crewai_tools import SerperDevTool


# ---------------------------------------------------------
# TOOL INITIALIZATION
# ---------------------------------------------------------

# This creates a web search tool using Serper API
# Agent will use this tool to search latest news
web_search_tool = SerperDevTool()


# ---------------------------------------------------------
# OUTPUT SCHEMA (VERY IMPORTANT)
# ---------------------------------------------------------

# Each single news item structure
class NewsItem(BaseModel):
    # Headline text
    headline: str = Field(description="Headline for the news")

    # URL of the news article
    url: str = Field(description="URL for the news webpage")

    # One paragraph summary
    news_summary: str = Field(description="Summary of the news")

    # News agency name
    news_agency_name: str = Field(description="Name of the news agency")


# Final output structure → list of 5 news items
class NewsReport(BaseModel):
    news: List[NewsItem]


# ---------------------------------------------------------
# CREW DEFINITION
# ---------------------------------------------------------

@CrewBase
class NewsReportCrew():
    """Crew that fetches and summarizes latest news"""

    # These will be auto-filled by CrewAI decorators
    agents: List[BaseAgent]
    tasks: List[Task]

    # YAML config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    # -----------------------------------------------------
    # AGENT
    # -----------------------------------------------------
    @agent
    def news_reporter(self) -> Agent:
        """
        Creates the agent responsible for searching and summarizing news
        """
        return Agent(
            config=self.agents_config['news_reporter'],  # reads YAML config
            verbose=True,                                # show logs
            tools=[web_search_tool],                     # allow web search
            max_iter=1,                                  # prevents looping
            temperature=0.2                              # stable output
        )


    # -----------------------------------------------------
    # TASK
    # -----------------------------------------------------
    @task
    def reporting_task(self) -> Task:
        """
        Defines what the agent should do
        """
        return Task(
            config=self.tasks_config['reporting_task'],  # YAML task instructions
            output_file="news.json",                     # saves output to file
            output_json=NewsReport                       # enforce JSON schema
        )


    # -----------------------------------------------------
    # CREW
    # -----------------------------------------------------
    @crew
    def crew(self) -> Crew:
        """
        Combines agents + tasks into a crew
        """
        return Crew(
            agents=self.agents,      # auto-collected agents
            tasks=self.tasks,        # auto-collected tasks
            process=Process.sequential,  # run tasks one by one
            verbose=True
        )