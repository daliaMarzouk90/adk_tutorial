"""Simple ADK starter agent for food recommendations."""

from dotenv import load_dotenv
from google.adk.agents import Agent
import google.auth

from .prompt import AGENT_INSTRUCTION
from .tools import recommend_meal

# Load local environment variables so ADK can access GOOGLE_API_KEY at runtime.
load_dotenv()

# Root ADK agent exposed by the API server and the Dev UI.
root_agent = Agent(
    name="food_recommendation_agent",
    model="gemini-2.0-flash",
    description="Recommends simple meals by cuisine and diet.",
    instruction=AGENT_INSTRUCTION,
    tools=[recommend_meal],
)
