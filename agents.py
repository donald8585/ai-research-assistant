from crewai import Agent
from crewai_tools import SerperDevTool
import os

os.environ["OPENAI_API_KEY"] = "NA"
os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"

search_tool = SerperDevTool()

def create_agents():
    researcher = Agent(
        role='Senior Research Analyst',
        goal='Conduct comprehensive research on {topic} and gather relevant factual information',
        backstory='You are an expert researcher with 10+ years of experience.',
        tools=[search_tool],
        verbose=True,
        allow_delegation=False,
        llm="ollama/llama3.1:latest"  # ← Changed to :latest
    )
    
    writer = Agent(
        role='Technical Content Writer',
        goal='Transform research findings into a clear, well-structured report on {topic}',
        backstory='You are an award-winning technical writer.',
        verbose=True,
        allow_delegation=False,
        llm="ollama/llama3.1:latest"  # ← Changed to :latest
    )
    
    critic = Agent(
        role='Quality Assurance Specialist',
        goal='Review and improve the report on {topic} for accuracy and completeness',
        backstory='You are a former scientific journal editor with high standards.',
        verbose=True,
        allow_delegation=False,
        llm="ollama/llama3.1:latest"  # ← Changed to :latest
    )
    
    return researcher, writer, critic
