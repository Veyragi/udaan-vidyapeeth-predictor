import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
df = pd.read_csv("CSAB ROUND 1 & ROUND 2.csv")

# Custom CSS for full-screen and styling
st.markdown(
    """
    <style>
    .reportview-container {
        max-width: 100%;
        padding: 0;
    }
    .sidebar .sidebar-content {
        background-color: #2e2e2e;
        color: white;
    }
    .css-1aumxhk {
        background-color: #1e1e1e;
        color: white;
    }
    .stTable {
        width: 100%;
        border-collapse: collapse;
    }
    .stTable th, .stTable td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    .stTable th {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Udaan Vidyapeeth College Predictor")

# Sidebar for filters
st.sidebar.header("Filters")
gender = st.sidebar.selectbox("Select Gender", options=["All"] + df["Gender"].unique().tolist())
institute = st.sidebar.selectbox("Select Institute", options=["All"] + df["Institute"].unique().tolist())
program = st.sidebar.selectbox("Select Program", options=["All"] + df["Academic Program Name"].unique().tolist())
quota = st.sidebar.selectbox("Select Quota", options=["All"] + df["Quota"].unique().tolist())
seat_type = st.sidebar.selectbox("Select Seat Type", options=["All"] + df["Seat Type"].unique().tolist())
rank_input = st.sidebar.number_input("Enter Your Main/Adv Rank", min_value=0, value=100000)

# Filter data based on selections
filtered_df = df.copy()
if gender != "All":
    filtered_df = filtered_df[filtered_df["Gender"] == gender]
if institute != "All":
    filtered_df = filtered_df[filtered_df["Institute"] == institute]
if program != "All":
    filtered_df = filtered_df[filtered_df["Academic Program Name"] == program]
if quota != "All":
    filtered_df = filtered_df[filtered_df["Quota"] == quota]
if seat_type != "All":
    filtered_df = filtered_df[filtered_df["Seat Type"] == seat_type]

# Filter based on rank (within Opening and Closing Rank range)
filtered_df = filtered_df[
    (filtered_df["Opening Rank"] <= rank_input) & (filtered_df["Closing Rank"] >= rank_input)
]

# Motivational message for high rank
if rank_input <= 20000:
    st.sidebar.markdown("**Congratulations! Your rank is excellent! Soar high with Udaan Vidyapeeth!**")
elif rank_input <= 50000:
    st.sidebar.markdown("**Great rank! You're on the path to success with Udaan Vidyapeeth!**")
elif rank_input <= 100000:
    st.sidebar.markdown("**Good effort! Keep pushing forward with Udaan Vidyapeeth!**")
else:
    st.sidebar.markdown("**Keep striving! Every step brings you closer to your goal with Udaan Vidyapeeth!**")

# Display filtered table
st.subheader("Eligible Colleges for Your Rank")
st.dataframe(filtered_df[["Institute", "Academic Program Name", "Quota", "Seat Type", "Gender", "Opening Rank", "Closing Rank"]])

# Optional: Add a visualization
if not filtered_df.empty:
    fig = px.bar(filtered_df, x="Institute", y="Opening Rank", title="Opening Ranks by Institute",
                 color="Gender", height=400)
    st.plotly_chart(fig)
else:
    st.write("No colleges found for your rank and filters. Try adjusting your rank or filters!")

