import streamlit as st
import pandas as pd

# Data: All Bets
data = {
    "Bet ID": [
        "325187498", "325188754", "325190199", "325191149", "325192733", 
        "325193503", "Parlay 2T", "Parlay 3T", "Parlay 3T", "G215916365", 
        "G215916886", "G215917287", "G215917700", "G215934883", "G215935425", 
        "G215936325", "G216024874", "G216025363", "G216027000", "325352698", 
        "325354961", "Win/Push 2T", "G216115030", "G216116205", "G216116859", 
        "G216117778", "G216119711", "G216120112", "G216121126", "G216146362", 
        "G216148050", "G216148584", "G216148715"
    ],
    "Description": [
        "Tyler Lockett Over 18.5 Rec Yds & Julian Love Over 5.5 Tackles",
        "Devon Witherspoon 6+ Tackles & Kevin Byard 7+ Tackles",
        "Tyler Lockett Over 1.5 Receptions & AJ Barner Over 9.5 Receiving Yards",
        "Over 42.5 Points (SEA@CHI) & DK Metcalf Longest Reception Over 24.5",
        "Devon Witherspoon 5+ Tackles, Kevin Byard 7+ Tackles, Over 42.5 (SEA@CHI)",
        "D'andre Swift 2+ Rec, AJ Barner Over 1.5 Rec, Rome Odunze Over 40.5 Rec Yds",
        "Chicago Bulls +6 (2H), Arkansas St/Bowling Grn U 27.5 (1H)",
        "Chicago Bulls +6 (2H), Bowling Green ML (1Q), Arkansas St/Bowling Grn U 27.5 (1H)",
        "Bulls/Hawks U 123.5 (2H), Arkansas St/Bowling Grn O 10.5 (1Q), Bowling Green ML (1H)",
        "Bowling Green U 34.5, Hawks/Bulls U 268.5",
        "Bucks/Nets O 209.5, Pelicans +18.5",
        "Grizzlies/Raptors U 281.5, Pelicans O 102.5",
        "Rockets U 125.5, Nets O 100.5",
        "Bears/Seahawks O 16.5, Kings/Pistons U 128.5 (1H)",
        "Kings/Pistons U 128.5 (1H), Trail Blazers/Jazz O 101 (1H)",
        "Jazz O 50.5 (1H), Kings/Pistons U 132.5 (1H)",
        "Vanderbilt vs Georgia Tech - Jamal Haynes TD",
        "Vanderbilt vs Georgia Tech - Junior Sherrill TD",
        "Brighton vs Brentford Draw, Vanderbilt/Georgia Tech O 44.5",
        "Tatum O 9.5 Reb, Morant O 23.5 Pts, Bridges O 16.5 Pts",
        "Taylen Green O 50.5 Rush Yds, Will Hammond U 1.5 Pass TDs, Rodney Hill U 53.5 Rush Yds",
        "Texas A&M/USC O 27.5 (1H), Syracuse/Wash St U 30 (1H)",
        "Suns/Mavericks O 190.5, Nuggets/Cavs U 273.5",
        "Clippers/Warriors O 199.5, Nuggets/Cavs U 271.5, Suns/Mavs O 191.5",
        "Suns +11.5, Cavs U 142.5",
        "Clippers/Warriors O 93.5 (1H), Nuggets U 129.5, Suns O 90.5",
        "Quentin Grimes O 7.5, Clippers/Warriors O 88.5 (1H)",
        "Klay Thompson O 9.5, James Harden O 16.5",
        "Suns ML, Trayce Jackson-Davis O 7.5 Reb",
        "USC/Texas A&M O 10.5 (3Q)",
        "San Diego Gulls ML, USC/Texas A&M O 14.5 (3Q)",
        "San Diego Gulls ML, USC Team Total O 17.5",
        "San Jose Sharks O 3.5, USC +7"
    ],
    "Risk ($)": [25, 25, 25, 25, 25, 25, 25, 25, 25, 50, 63, 61, 50, 50, 104, 95, 50, 25, 117, 156, 25, 19, 25, 70, 50, 50, 121, 114, 25, 56, 175, 50, 50],
    "Outcome": [
        "Loss", "Loss", "Loss", "Loss", "Loss", "Loss", "Loss", "Loss", "Loss", 
        "Loss", "Win", "Win", "Loss", "Loss", "Win", "Win", "Win", "Loss", 
        "Win", "Win", "Loss", "Loss", "Loss", "Loss", "Loss", "Win", "Win", 
        "Loss", "Win", "Win", "Pending", "Pending"
    ],
    "Net Profit ($)": [
        -25, -25, -25, -25, -25, -25, -25, -25, -25, -50, 63, 61, -50, -50, 
        104, 95, 50, -25, 117, 156, -25, -19, -25, -70, -50, -50, 121, 114, 
        -25, 56, 175, 0, 0
    ],
    "To Win ($)": [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 61, 0, 0, 104, 95, 50, 0, 117, 156, 
        0, 0, 0, 0, 0, 0, 121, 114, 0, 56, 175, 136, 136
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Dashboard Title
st.title("📊 Bet Tracker Dashboard")

# Overview Section
st.header("Overview")
total_wagers = len(df)
total_risk = df["Risk ($)"].sum()
net_profit = df["Net Profit ($)"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Wagers", total_wagers)
col2.metric("Total Risk ($)", f"${total_risk}")
col3.metric("Net Profit ($)", f"${net_profit}")

# Full Bet Summary
st.header("All Bets Summary")
st.dataframe(df)

# Filters Section
st.sidebar.header("Filters")
status_filter = st.sidebar.multiselect(
    "Filter by Outcome",
    options=df["Outcome"].unique(),
    default=df["Outcome"].unique(),
)

# Filtered Data
filtered_df = df[df["Outcome"].isin(status_filter)]
st.subheader("Filtered Bets")
st.dataframe(filtered_df)

# Pending Bets
st.header("Pending Bets")
pending_bets = df[df["Outcome"] == "Pending"]
if not pending_bets.empty:
    st.dataframe(pending_bets)
else:
    st.write("No pending bets.")

# Charts
st.header("Charts")
st.subheader("Outcome Breakdown")
outcome_chart = df.groupby("Outcome")["Risk ($)"].sum()
st.bar_chart(outcome_chart)

st.subheader("Net Profit Trend")
st.line_chart(df["Net Profit ($)"])

# Footer
st.write("---")
st.write("🎯 Developed with ❤️ by Bet Tracker")