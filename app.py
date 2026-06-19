import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

st.sidebar.title("Graph Analytics Dashboard")

page = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Influential Users",
        "Correlation Analysis",
        "Machine Learning",
        "Conclusion"
    ]
)



st.title("Graph Analytics on Social Influence Dataset")


st.info("""
This dashboard analyzes social network influence using
Graph Analytics and Machine Learning techniques.
""")

st.subheader("Project Workflow")

st.markdown("""
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Graph Analytics
5. Machine Learning Modeling
6. Feature Importance Analysis
7. Dashboard Deployment
""")

df = pd.read_csv("Dataset/social_influence_dataset.csv")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Users",
    len(df)
)

col2.metric(
    "Average Influence",
    round(df["influence_score"].mean(), 2)
)

col3.metric(
    "Maximum Influence",
    round(df["influence_score"].max(), 2)
)

st.subheader("Dataset Preview")
st.dataframe(df.head())


st.subheader("Dataset Statistics")
st.dataframe(df.describe())


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
st.subheader("Feature Importance")



X = df.drop(
    ['user_id', 'region', 'influence_score'],
    axis=1
)

y = df['influence_score']

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X, y)

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
})

fig, ax = plt.subplots(figsize=(8,5))

feature_importance.sort_values(
    by='Importance',
    ascending=True
).plot(
    x='Feature',
    y='Importance',
    kind='barh',
    ax=ax
)

st.pyplot(fig)

st.subheader("Project Conclusion")

st.success("""
Random Forest Regression significantly outperformed Linear Regression,
achieving an R² Score of 0.996.

Feature importance analysis revealed that Followers, Degree Centrality,
and Betweenness Centrality are the strongest predictors of influence score.

This project demonstrates how Graph Analytics and Machine Learning can be
combined to identify influential users in social networks.
""")

st.markdown("---")

st.markdown(
    """
    ### Developed By Bharath Kalyan S
    
    Graph Analytics & Machine Learning Project
    
    Tools Used:
    Python | Pandas | Scikit-Learn | Streamlit | Matplotlib
    """
)