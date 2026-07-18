import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("world_cup_data.csv")

df["Goals"] = df["Top Team Scorer"].str.extract(r"(\d+)$").astype(int)
df["Player"] = df["Top Team Scorer"].str.replace(r"\s*-\s*\d+$", "", regex=True)

goals = df.sort_values(by="Goals", ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(data=goals, x="Goals", y="Top Team Scorer", hue="Squad")
plt.show()