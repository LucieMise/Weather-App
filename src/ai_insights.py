import ollama
import pandas as pd


def generate_weather_insights(df: pd.DataFrame):

    # Limit dataset size
    sample = df.tail(100)

    dataset = sample.to_csv(index=False)

    prompt = f"""
You are a weather data analyst.

Analyze the following weather dataset and provide insights.

Dataset:
{dataset}

Provide:

1. Temperature trends
2. Humidity patterns
3. Unusual weather patterns
4. Predictions for the coming days
5. Advice for travelers
"""

    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]