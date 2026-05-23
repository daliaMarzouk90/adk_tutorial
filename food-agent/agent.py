"""Simple ADK starter agent for food recommendations."""

from dotenv import load_dotenv
from google.adk.agents import Agent

# Load local environment variables so ADK can access GOOGLE_API_KEY at runtime.
load_dotenv()


def recommend_meal(cuisine: str, diet: str) -> str:
    """Tool: return a simple meal recommendation based on cuisine and diet."""
    cuisine_key = cuisine.strip().lower()
    diet_key = diet.strip().lower()

    recommendations = {
        ("egyptian", "vegan"): "Koshari",
        ("egyptian", "protein"): "Hawawshi",
        ("italian", "vegan"): "Pasta al Pomodoro (without cheese)",
        ("italian", "protein"): "Chicken Piccata",
    }

    meal = recommendations.get((cuisine_key, diet_key))
    if meal:
        return f"Recommended meal: {meal}."

    # Runtime fallback keeps responses beginner-friendly when no exact mapping is found.
    return (
        "I couldn't find an exact match. Try one of: "
        "Egyptian/Italian with vegan/protein preferences."
    )


# Root ADK agent exposed by the API server and the Dev UI.
root_agent = Agent(
    name="food_recommendation_agent",
    model="gemini-2.0-flash",
    description="Recommends simple meals by cuisine and diet.",
    instruction=(
        "You are a helpful food recommendation assistant. "
        "Collect cuisine and diet preferences, then call recommend_meal tool. "
        "Keep answers concise and practical for beginners."
    ),
    tools=[recommend_meal],
)
