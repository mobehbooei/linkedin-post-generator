from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os


load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

researcher = Agent(
    role='researcher',
    goal='research new AI insights',
    backstory='You are an AI research assistant.',
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role='writer',
    goal='write compelling and engaging blog posts about AI trends and insights',
    backstory='You are an AI blog post writer who specializes in writing about AI topics.',
    verbose=True,
    allow_delegation=False
)

task1 = Task(description='Investigate the latest AI trends', expected_output='A bullet list of 4 most important AI trends', agent=researcher)
task2 = Task(description='Write a compelling blog post based on the latest AI trends', expected_output='A linkedin optimized blog post', agent=writer)

crew = Crew(
    agents=[researcher, writer], 
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()