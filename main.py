import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o")

# Tools
search_tool = DuckDuckGoSearchRun()

def run_research(topic: str):
    # 1. Define Agents
    researcher = Agent(
        role="Senior Research Analyst",
        goal=f"Explore and analyze deep-dive information on {topic}. Uncover breakthrough insights.",
        backstory="You are a veteran researcher with a PhD in Computer Science. You thrive on finding hidden gems of information.",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool],
        llm=llm
    )

    writer = Agent(
        role="Technical Content Writer",
        goal=f"Transform the research findings into a professional, engaging, and structured report on {topic}.",
        backstory="You are a senior editor at a top tech publication. You know how to make complex tech topics accessible and engaging.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    critic = Agent(
        role="Quality Assurance Specialist",
        goal=f"Critically review the research report on {topic} for accuracy, tone, and completeness.",
        backstory="You are an expert fact-checker and editor with a sharp eye for detail. You ensure nothing but perfection.",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )

    # 2. Define Tasks
    research_task = Task(
        description=f"Conduct thorough research on {topic}. Look for the latest trends, data, and expert opinions.",
        agent=researcher,
        expected_output="A comprehensive summary of research findings, including at least 5 key insights and supporting data."
    )

    writing_task = Task(
        description=f"Write a 5-section research report based on the findings. Include an executive summary and forward-looking conclusions.",
        agent=writer,
        expected_output="A high-quality Markdown report ready for professional presentation."
    )

    review_task = Task(
        description=f"Review the report for factual consistency and professional tone. Provide suggestions for refinement.",
        agent=critic,
        expected_output="A finalized, polished research report in Markdown format."
    )

    # 3. Form the Crew
    research_crew = Crew(
        agents=[researcher, writer, critic],
        tasks=[research_task, writing_task, review_task],
        process=Process.sequential,
        verbose=True
    )

    # 4. Kickoff
    result = research_crew.kickoff()
    return result

if __name__ == "__main__":
    # Sample Mock Run
    print(run_research(topic="The Future of AI Agents in Enterprise Software (2025-2027)"))