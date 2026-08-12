import sqlite3
import pandas as pd
import streamlit as st


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="RetailVisionAI",
    page_icon="👁️",
    layout="wide"
)


# -----------------------------
# Database connection
# -----------------------------

DATABASE_FILE = "data/database/retailvision.db"


def load_sessions():
    """Load all customer sessions from SQLite."""

    connection = sqlite3.connect(DATABASE_FILE)

    query = """
        SELECT
            id,
            start_time,
            end_time,
            attentive_time,
            away_time,
            attention_rate
        FROM sessions
        ORDER BY id
    """

    data = pd.read_sql_query(query, connection)

    connection.close()

    return data


# -----------------------------
# Dashboard title
# -----------------------------

st.title("RetailVisionAI")
st.subheader("Customer Attention Analytics")

st.write(
    "Computer vision based analysis of customer attention "
    "using MediaPipe and head pose estimation."
)


# -----------------------------
# Load data
# -----------------------------

sessions = load_sessions()


# -----------------------------
# Check if data exists
# -----------------------------

if sessions.empty:

    st.warning("No customer sessions have been recorded yet.")

else:

    # -----------------------------
    # Calculate dashboard metrics
    # -----------------------------

    total_sessions = len(sessions)

    average_attention = sessions["attention_rate"].mean()

    average_attentive_time = sessions["attentive_time"].mean()

    average_away_time = sessions["away_time"].mean()


    # -----------------------------
    # Metric cards
    # -----------------------------

    column1, column2, column3, column4 = st.columns(4)

    column1.metric(
        "Total Sessions",
        total_sessions
    )

    column2.metric(
        "Average Attention",
        f"{average_attention:.1f}%"
    )

    column3.metric(
        "Average Attentive Time",
        f"{average_attentive_time:.1f}s"
    )

    column4.metric(
        "Average Looking Away",
        f"{average_away_time:.1f}s"
    )


    st.divider()


    # -----------------------------
    # Attention rate chart
    # -----------------------------

    st.subheader("Attention Rate by Session")

    chart_data = sessions.set_index("id")[
        ["attention_rate"]
    ]

    st.line_chart(chart_data)


    # -----------------------------
    # Attention time chart
    # -----------------------------

    st.subheader("Attentive Time vs Looking Away Time")

    time_data = sessions.set_index("id")[
        ["attentive_time", "away_time"]
    ]

    st.bar_chart(time_data)


    # -----------------------------
    # Session history
    # -----------------------------

    st.subheader("Session History")

    display_data = sessions.copy()

    display_data["attentive_time"] = (
        display_data["attentive_time"].round(1)
    )

    display_data["away_time"] = (
        display_data["away_time"].round(1)
    )

    display_data["attention_rate"] = (
        display_data["attention_rate"].round(1)
    )

    st.dataframe(
        display_data,
        use_container_width=True
    )