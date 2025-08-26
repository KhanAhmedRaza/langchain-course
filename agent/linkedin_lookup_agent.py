
import os
import sys
from dotenv import load_dotenv
try:
    from tools.tools import get_profile_url_tavily
except ModuleNotFoundError:
    # Add project root to sys.path and try again
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from tools.tools import get_profile_url_tavily

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

def lookup(name:str) ->str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
    )
    #return "https://www.linkedin.com/in/khanahmedraza/";
    template = """given the full name {name_of_person} I want you to get it me a link to their
    LinkedIn profile page. Your answer should only contain the URL without any additional text."""
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"],
        template=template
    )
    tools_for_agent = [
        Tool(
            name="Crawl google 4 Linkedin profile page",
            description="Given a person's full name, ONLY return the direct LinkedIn profile URL as a string. Do not include any other text, explanation, or formatting.",
            func=get_profile_url_tavily,
            args={"prompt": prompt_template}
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_url = result["output"]
    return linkedin_url

