from streamlit_autorefresh import st_autorefresh
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ================= PAGE SETTINGS =================

st.set_page_config(
    page_title="AI Classroom Intelligence",

    layout="wide"
)
# ⭐ Auto refresh every 3 seconds (3000 milliseconds)
st_autorefresh(interval=3000, key="dashboardrefresh")

st.title("AI Classroom Intelligence Dashboard")

# ================= CONNECT DATABASE =================
# This ensures correct path even if folder moves
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

db_path = os.path.join(BASE_DIR, "data", "attendance.db")

conn = sqlite3.connect(db_path)

# ================= LOAD DATA =================
query = "SELECT * FROM attention"
df = pd.read_sql(query, conn)

# ================= INPUT BOX =================

student_id = st.text_input(
    "Enter Student ID", value="STU001", max_chars=10
)


# ================= FILTER DATA =================

student = df[df["student_id"] == student_id]


if student.empty:

    st.warning("No data found")

else:

    # Filter noise

    attentive = student[

        (student["status"] == "Attentive") &

        (student["duration"] >= 2)

    ]["duration"].sum()


    sleeping = student[

        (student["status"] == "Sleeping") &

        (student["duration"] >= 5)

    ]["duration"].sum()


    total = attentive + sleeping


    if total == 0:

        st.warning("No valid data")

    else:

        attention_score = attentive / total * 100


        engagement_score = (

            attention_score * 0.7 +

            (100 - sleeping / total * 100) * 0.3

        )


        # ================= METRICS =================

        col1, col2 = st.columns(2)


        col1.metric(

            "Attention Score",

            f"{attention_score:.2f}%"

        )


        col2.metric(

            "Engagement Score",

            f"{engagement_score:.2f}%"

        )


        # ================= GRAPHS =================
        left, right = st.columns(2)
        # PIE CHART
        with left:
            st.subheader("Attention Distribution")
            fig1, ax1 = plt.subplots(
                figsize=(2,4)   # Change size here
            )
            ax1.pie(
                [attentive, sleeping], labels=["Attentive","Sleeping"],
                autopct="%1.1f%%", colors=["green","red"]
            )

            st.pyplot(fig1)
        # BAR CHART
        with right:

            st.subheader("Performance Scores")
            fig2, ax2 = plt.subplots(
                figsize=(6,4)   # Change size here
            )


            sns.barplot(
                x=["Attention","Engagement"], y=[attention_score, engagement_score],
                hue=["Attention","Engagement"], legend=False, palette=["green","blue"], ax=ax2
            )
            ax2.set_ylim(0,100)


            st.pyplot(fig2)

# ================= CLASS OVERVIEW =================
st.divider()

st.header("Class Overview")


# Load full data again

query = "SELECT * FROM attention"

df = pd.read_sql(query, conn)


if df.empty:

    st.warning("No class data available")

else:

    summary = []

    students = df["student_id"].unique()


    for sid in students:


        student = df[df["student_id"] == sid]


        attentive = student[
            student["status"] == "Attentive"
        ]["duration"].sum()


        sleeping = student[
            student["status"] == "Sleeping"
        ]["duration"].sum()


        total = attentive + sleeping


        if total == 0:
            continue


        attention_score = attentive / total * 100


        engagement_score = (

            attention_score * 0.7 +

            (100 - sleeping / total * 100) * 0.3

        )


        summary.append({

            "Student ID": sid,

            "Attention %": round(attention_score,2),

            "Engagement %": round(engagement_score,2)

        })


    class_df = pd.DataFrame(summary)


    class_df = class_df.sort_values(

        by="Engagement %",

        ascending=False

    )


    # ================= SHOW TABLE =================


    st.subheader("Class Ranking")
    st.dataframe(class_df, width="stretch")


    # ================= TOP STUDENT =================


    topper = class_df.iloc[0]


    st.success(

        f"🏆 Top Student: {topper['Student ID']} "

        f"({topper['Engagement %']}%)"

    )


    # ================= LOWEST STUDENT =================


    lowest = class_df.iloc[-1]


    st.error(

        f"⚠ Needs Attention: {lowest['Student ID']} "

        f"({lowest['Engagement %']}%)"

    )


    # ================= BAR GRAPH =================
    st.subheader("Class Performance")
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(
        x="Student ID", y="Engagement %", hue="Student ID", data=class_df, legend=False, palette="viridis", ax=ax
    )
    ax.set_ylim(0,100)
    st.pyplot(fig)
# ================= CLOSE DATABASE =================
conn.close()
