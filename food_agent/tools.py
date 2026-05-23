"""Tool functions for the food recommendation ADK agent."""


def recommend_meal(cuisine: str, diet: str) -> str:
    """Return a simple meal recommendation based on cuisine and diet."""
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

    return (
        "I couldn't find an exact match. Try one of: "
        "Egyptian/Italian with vegan/protein preferences."
    )
