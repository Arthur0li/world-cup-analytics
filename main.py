import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="World Cup Dashboard",
    page_icon="⚽",
    layout="wide"
)

# Streamlit CSS
st.markdown("""
<style>
    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #A0A0A0;
        margin-bottom: 30px;
    }

    /* Tab text */
    button[data-baseweb="tab"] {
        font-size: 15px;
        font-weight: 500;
    }

    /* Reduce empty space around the page */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">⚽ World Cup Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'International football performance analysis'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

df = pd.read_csv("world_cup_data.csv")

df["Goals"] = (
    df["Top Team Scorer"]
    .str.extract(r"(\d+)$")
    .astype(int)
)

df["Player"] = (
    df["Top Team Scorer"]
    .str.replace(r"\s*-\s*\d+$", "", regex=True)
)


# ---------------------------------------------------------
# SORT DATA
# ---------------------------------------------------------

goals = df.sort_values(by="Goals", ascending=False)
wins = df.sort_values(by="W", ascending=False)
draws = df.sort_values(by="D", ascending=False)
losses = df.sort_values(by="L", ascending=False)
goals_team = df.sort_values(by="GF", ascending=False)
goals_conceded = df.sort_values(by="GA", ascending=False)
difference = df.sort_values(by="GD", ascending=False)


# ---------------------------------------------------------
# VISUAL STYLE
# ---------------------------------------------------------

sns.set_theme(
    style="whitegrid",
    font_scale=1
)


# ---------------------------------------------------------
# REUSABLE CHART FUNCTION
# ---------------------------------------------------------

def create_bar_chart(
    data,
    x,
    y,
    title,
    xlabel,
    color="#4EA1D3"
):

    data = data.sort_values(by=x, ascending=False)

    fig, ax = plt.subplots(
        figsize=(14, 13)
    )

    # Dark background
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")

    # Bar chart
    bars = sns.barplot(
        data=data,
        x=x,
        y=y,
        ax=ax,
        color=color,
        edgecolor="none"
    )

    # Title
    ax.set_title(
        title,
        fontsize=20,
        fontweight="bold",
        color="white",
        loc="left",
        pad=20
    )

    # Axis labels
    ax.set_xlabel(
        xlabel,
        fontsize=12,
        color="#B8B8B8",
        labelpad=10
    )

    ax.set_ylabel("")

    # Tick labels
    ax.tick_params(
        axis="x",
        colors="#AFAFAF",
        labelsize=10
    )

    ax.tick_params(
        axis="y",
        colors="#FFFFFF",
        labelsize=11
    )

    # Grid
    ax.grid(
        axis="x",
        linestyle="--",
        linewidth=0.6,
        alpha=0.2,
        color="white"
    )

    ax.grid(
        axis="y",
        visible=False
    )

    # Remove borders
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#333333")

    # Add values to bars
    for bar in bars.patches:

        width = bar.get_width()

        ax.text(
            width + (data[x].max() * 0.01),
            bar.get_y() + bar.get_height() / 2,
            f"{int(width)}",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="white"
        )

    # Better spacing
    plt.tight_layout()

    return fig


# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏆 Wins",
    "🤝 Draws",
    "❌ Losses",
    "⚽ Goals Scored",
    "🥅 Goals Conceded",
    "📈 Goal Difference",
    "👑 Top Scorers"
])


# ---------------------------------------------------------
# WINS
# ---------------------------------------------------------

with tab1:

    fig = create_bar_chart(
        data=wins,
        x="W",
        y="Squad",
        title="🏆 Wins by Team",
        xlabel="Number of Wins",
        color="#4EA1D3"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------------
# DRAWS
# ---------------------------------------------------------

with tab2:

    fig = create_bar_chart(
        data=draws,
        x="D",
        y="Squad",
        title="🤝 Draws by Team",
        xlabel="Number of Draws",
        color="#F0B35B"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------------
# LOSSES
# ---------------------------------------------------------

with tab3:

    fig = create_bar_chart(
        data=losses,
        x="L",
        y="Squad",
        title="❌ Losses by Team",
        xlabel="Number of Losses",
        color="#E76F6F"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------------
# GOALS SCORED
# ---------------------------------------------------------

with tab4:

    fig = create_bar_chart(
        data=goals_team,
        x="GF",
        y="Squad",
        title="⚽ Goals Scored by Team",
        xlabel="Goals Scored",
        color="#65B891"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------------
# GOALS CONCEDED
# ---------------------------------------------------------

with tab5:

    fig = create_bar_chart(
        data=goals_conceded,
        x="GA",
        y="Squad",
        title="🥅 Goals Conceded by Team",
        xlabel="Goals Conceded",
        color="#C77DFF"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------------
# GOAL DIFFERENCE
# ---------------------------------------------------------

with tab6:

    fig = create_bar_chart(
        data=difference,
        x="GD",
        y="Squad",
        title="📈 Goal Difference by Team",
        xlabel="Goal Difference",
        color="#5DADE2"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------------
# TOP SCORERS
# ---------------------------------------------------------

with tab7:

    fig = create_bar_chart(
        data=goals,
        x="Goals",
        y="Top Team Scorer",
        title="👑 Top Team Scorers",
        xlabel="Goals",
        color="#D4AF37"
    )

    st.pyplot(
        fig,
        use_container_width=True
    )