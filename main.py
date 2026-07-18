import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="World Cup Dashboard", layout="wide")
st.title("World Cup Dashboard")

df = pd.read_csv("world_cup_data.csv")

df["Goals"] = df["Top Team Scorer"].str.extract(r"(\d+)$").astype(int)
df["Player"] = df["Top Team Scorer"].str.replace(r"\s*-\s*\d+$", "", regex=True)

goals = df.sort_values(by="Goals", ascending=False)
wins = df.sort_values(by="W", ascending=False)
draws = df.sort_values(by="D", ascending=False)
losses = df.sort_values(by="L", ascending=False)
goals_team = df.sort_values(by="GF", ascending=False)
goals_conceded = df.sort_values(by="GA", ascending=False)
difference = df.sort_values(by="GD", ascending=False)

# Create the tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏆 Wins",
    "🤝 Draws",
    "❌ Losses",
    "⚽ Goals Scored",
    "🥅 Goals Conceded",
    "📈 Goal Difference",
    "👑 Top Scorers"
])

# WINS
with tab1:
    st.header("Wins")
    fig, ax = plt.subplots(figsize=(15, 20))
    sns.barplot(data=wins, x="W", y="Squad")
    ax.set_xlabel("Wins")
    ax.set_ylabel("Teams")
    st.pyplot(fig)

# DRAWS
with tab2:
    st.header("Draws")
    fig, ax = plt.subplots(figsize=(15, 20))
    sns.barplot(data=draws, x="D", y="Squad")
    ax.set_xlabel("Draws")
    ax.set_ylabel("Teams")
    st.pyplot(fig)

# LOSSES
with tab3:
    st.header("Losses")
    fig, ax = plt.subplots(figsize=(15, 20))
    sns.barplot(data=losses, x="L", y="Squad")
    ax.set_xlabel("Losses")
    ax.set_ylabel("Teams")
    st.pyplot(fig)

# GOALS SCORED
with tab4:
    st.header("Goals Scored")
    fig, ax = plt.subplots(figsize=(15, 20))
    sns.barplot(data=goals_team, x="GF", y="Squad")
    ax.set_xlabel("Goals_team")
    ax.set_ylabel("Teams")
    st.pyplot(fig)

# GOALS CONCEDED
with tab5:
    st.header("Goals Conceded")
    fig, ax = plt.subplots(figsize=(15, 20))
    sns.barplot(data=goals_conceded, x="GA", y="Squad")
    ax.set_xlabel("Goals_conceded")
    ax.set_ylabel("Teams")
    st.pyplot(fig)

# GOAL DIFFERENCE
with tab6:
    st.header("Goal Difference")
    fig, ax = plt.subplots(figsize=(15, 20))
    sns.barplot(data=difference, x="GD", y="Squad")
    ax.set_xlabel("difference")
    ax.set_ylabel("Teams")
    st.pyplot(fig)

# TOP SCORERES
with tab7:
    st.header("Top Scorers")
    fig, ax = plt.subplots(figsize=(15, 20))
    sns.barplot(data=goals, x="Goals", y="Top Team Scorer")
    ax.set_xlabel("Goals")
    ax.set_ylabel("Top Scorers")
    st.pyplot(fig)
