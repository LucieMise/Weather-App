import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from src.ai_insights import generate_weather_insights

engine = create_engine("sqlite:///data/weather.db")

st.title("Weather Analytics Dashboard")

query = "SELECT * FROM weather_history"

df = pd.read_sql(query, engine)

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.write(df)

st.header("Temperature Trends")

fig = px.line(
    df,
    x="timestamp",
    y="temperature",
    color="city"
)

st.plotly_chart(fig)

st.header("Humidity Patterns")

fig = px.line(
    df,
    x="timestamp",
    y="humidity",
    color="city"
)

st.plotly_chart(fig)

st.header("Hottest Cities")

hottest = (
    df.groupby("city")["temperature"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(hottest)


st.header("Coldest Days")

coldest = df.nsmallest(10, "temperature")

st.write(coldest[["city", "temperature", "timestamp"]])

st.header("AI Weather Insights")

if st.button("Generate AI Insights"):

    insights = generate_weather_insights(df)

    st.write(insights)



