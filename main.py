from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent
from dotenv import load_dotenv 
import os

load_dotenv()


# Seting the model
llm = ChatOpenAI(model=os.getenv("AI_MODEL"),
                 api_key=os.getenv("AI_API_KEY"),
                 base_url=os.getenv("AI_ENDPOINT"),
                 temperature=0)


# setting up the tools
@tool
def search_news(query: str):
    """Searches the internet for the latest news and real time updates"""
    search =TavilySearchResults(max_results=1)
    return search.invoke(query)


# creating the agent
agent = create_agent(model = llm, tools = [search_news], system_prompt="You are a professional research assistant . use tools to get accurate information")


# excetuting the agent
response = agent.invoke({
    "messages":[("human", "what is the latest news about hantavirus in sentence?")]
})

print("AI Response:", response["messages"][-1].content)