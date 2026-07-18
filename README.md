<img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=112A46&text=World%20Cup%20Dashboard&textBg=false&animation=fadeIn&fontColor=ACC8E5"/>

# World Cup Dashboard

An interactive dashboard built with **Streamlit**, **Pandas**, **Matplotlib**, and **Seaborn** to explore World Cup team statistics in a clean and visual way.

The project organizes the data into tabs so you can compare team performance by wins, draws, losses, goals scored, goals conceded, goal difference, and top scorers.

---

## ✨ Features

* 🏆 **Wins tab** to compare the teams with the most victories.
* 🤝 **Draws tab** to analyze how many matches each team drew.
* ❌ **Losses tab** to review the teams with the most defeats.
* ⚽ **Goals scored tab** to rank teams by goals scored.
* 🥅 **Goals conceded tab** to compare defensive performance.
* 📈 **Goal difference tab** to highlight the strongest overall teams.
* 👑 **Top scorers tab** to display the players with the highest number of goals.

---

## 🚀 Technologies Used

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" />
<img src="https://img.shields.io/badge/Seaborn-5A9BD5?style=for-the-badge&logo=seaborn&logoColor=white" />

</div>

---

## 🛠️ Installation

If you'd like to run the project locally:

```bash
git clone https://github.com/username/world-cup-dashboard.git

cd world-cup-dashboard
```

Install the dependencies:

```bash
pip install streamlit pandas matplotlib seaborn
```

Then run the app:

```bash
streamlit run app.py
```

Make sure the `world_cup_data.csv` file is inside the project folder.

---

## 📖 How It Works

The app loads the dataset and prepares new columns for analysis, including the number of goals scored by each top scorer.

Then it organizes the data into ranked tables and displays them in separate tabs:

1. 🏆 **Wins** — teams sorted by wins.
2. 🤝 **Draws** — teams sorted by draws.
3. ❌ **Losses** — teams sorted by losses.
4. ⚽ **Goals Scored** — teams sorted by goals scored.
5. 🥅 **Goals Conceded** — teams sorted by goals conceded.
6. 📈 **Goal Difference** — teams sorted by goal difference.
7. 👑 **Top Scorers** — players sorted by goals.

Each tab renders its own bar chart using Seaborn and Matplotlib inside Streamlit.

---

## 📚 What I Learned

This project helped me improve my knowledge of:

* Python for data analysis
* Streamlit for interactive dashboards
* Pandas for data manipulation
* Matplotlib and Seaborn for data visualization
* Organizing multiple visualizations in a single application

---

## 👨‍💻 Author

Developed by **Arthur Oliveira**.

📫 Connect with me:

* 💼 LinkedIn: https://www.linkedin.com/in/arthur-oliveira-21ab8a236/?locale=en
* 🐙 GitHub: https://github.com/Arthur0li

---

## ⭐ Support

If you enjoyed this project, consider giving it a star on GitHub!

<img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=112A46&section=footer"/>
