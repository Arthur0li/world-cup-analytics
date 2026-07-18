import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="World Cup Dashboard", layout="wide")
st.title("Gráfico de artilheiros da Copa")

df = pd.read_csv("world_cup_data.csv")

df["Goals"] = df["Top Team Scorer"].str.extract(r"(\d+)$").astype(int)
df["Player"] = df["Top Team Scorer"].str.replace(r"\s*-\s*\d+$", "", regex=True)

goals = df.sort_values(by="Goals", ascending=False)

fig, ax = plt.subplots(figsize=(15, 20))
sns.barplot(data=goals, x="Goals", y="Top Team Scorer", hue="Squad", ax=ax)
ax.set_title("Top Team Scorer por gols")
ax.set_xlabel("Goals")
ax.set_ylabel("Top Team Scorer")

st.pyplot(fig)