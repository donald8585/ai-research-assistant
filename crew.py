from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

def run_research_crew(topic):
    """
    Orchestrates the multi-agent research workflow
    """
    researcher, writer, critic = create_agents()
    tasks = create_tasks(researcher, writer, critic, topic)
    
    crew = Crew(
        agents=[researcher, writer, critic],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        memory=False  # ← ADD THIS LINE - Disable memory for Ollama
    )
    
    result = crew.kickoff()
    return result
