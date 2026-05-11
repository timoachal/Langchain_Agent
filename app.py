import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent
from dotenv import load_dotenv 
import os

load_dotenv()


# setting up the streamlit ui
st.set_page_config(page_title="Ai research assistant")
st.title("Professional Research Assistant")
st.write("Ask a question to search the latest news and real time updates")

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

# streamlit interaction

user_query = st.text_input("Enter your question here:", placeholder="e.g what is the latest news")


if st.button("Run Research"):
    if user_query:
        with st.spinner("Researching..."):
            response = agent.invoke({
                "messages":[("human", user_query)]
            })

            st.subheader("AI Response:")
            st.write(response["messages"][-1].content)
    else:
        st.warning("Please enter a question to research.")        