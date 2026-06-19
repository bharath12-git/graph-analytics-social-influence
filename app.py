import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Graph Analytics on Social Influence Dataset")

df = pd.read_csv(
    "Dataset/social_influence_dataset.csv"
)

# KPI CARDS
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Users",
    len(df)
)

col2.metric(
    "Average Influence Score",
    round(df["influence_score"].mean(), 2)
)

col3.metric(
    "Maximum Influence Score",
    round(df["influence_score"].max(), 2)
)

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Distribution of Influence Score")

fig, ax = plt.subplots(figsize=(8,5))

ax.hist(
    df["influence_score"],
    bins=30
)

ax.set_title("Distribution of Influence Score")
ax.set_xlabel("Influence Score")
ax.set_ylabel("Frequency")

st.pyplot(fig)


st.subheader("Top 10 Influential Users")

top10 = df.nlargest(
    10,
    "influence_score"
)

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    top10["user_id"],
    top10["influence_score"]
)

ax.set_title("Top 10 Influential Users")
ax.set_xlabel("User ID")
ax.set_ylabel("Influence Score")

plt.xticks(rotation=45)

st.pyplot(fig)


st.subheader("Top 10 Influential Users")

top10 = df.nlargest(
    10,
    "influence_score"
)

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    top10["user_id"],
    top10["influence_score"]
)

ax.set_title("Top 10 Influential Users")
ax.set_xlabel("User ID")
ax.set_ylabel("Influence Score")

plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader("Correlation Matrix")

fig, ax = plt.subplots(figsize=(12,8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)


st.subheader("Random Forest Regression Performance")

col1, col2, col3 = st.columns(3)

col1.metric(
    "MAE",
    "0.41"
)

col2.metric(
    "MSE",
    "0.46"
)

col3.metric(
    "R² Score",
    "0.996"
)


st.subheader("Project Conclusion")

st.success("""
Random Forest Regression significantly outperformed Linear Regression,
achieving an R² Score of 0.996.

Feature importance analysis revealed that Followers, Degree Centrality,
and Betweenness Centrality are the strongest predictors of influence score.

This project demonstrates how Graph Analytics and Machine Learning can be
combined to identify influential users in social networks.
""")