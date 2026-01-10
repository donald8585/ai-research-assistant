from crewai import Task

def create_tasks(researcher, writer, critic, topic):
    research_task = Task(
        description=f"""Research the topic: {topic}

        Your tasks:
        1. Search for the latest information about {topic}
        2. Gather key facts, statistics, and insights
        3. Identify credible sources
        4. Summarize findings in bullet points

        Focus on accuracy and relevance.""",
        agent=researcher,
        expected_output='A comprehensive list of research findings with sources'
    )

    write_task = Task(
        description=f"""Using the research findings, write a detailed report on: {topic}

        Your report should include:
        1. Executive Summary (2-3 sentences)
        2. Key Findings (structured sections)
        3. Important Details (with context)
        4. Conclusion

        Use clear headings and professional tone.""",
        agent=writer,
        expected_output='A well-structured markdown report',
        context=[research_task]
    )

    critique_task = Task(
        description=f"""Review the report on {topic} and provide final polished version.

        Check for:
        1. Factual accuracy
        2. Logical flow and structure
        3. Clarity and readability
        4. Completeness of information

        Provide the FINAL improved report, not just critique notes.""",
        agent=critic,
        expected_output='A polished, publication-ready report in markdown format',
        context=[research_task, write_task]
    )

    return [research_task, write_task, critique_task]
