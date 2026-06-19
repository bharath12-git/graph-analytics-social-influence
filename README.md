# Graph Analytics on Social Influence Dataset

## Project Overview

This project analyzes a social influence dataset using Exploratory Data Analysis (EDA), Graph Analytics, and Machine Learning techniques to identify influential users and predict influence scores.

The objective is to understand how user attributes, engagement metrics, and network centrality measures contribute to influence within a social network.



## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook



## Dataset Features

The dataset contains user-level social network information including:

* User ID
* Followers
* Following
* Posts
* Likes Received
* Comments Received
* Mentions
* Shares
* Account Age (Days)
* Engagement Rate
* Degree Centrality
* Betweenness Centrality
* Influence Score



## Project Workflow

### 1. Data Loading and Preprocessing

* Loaded the dataset using Pandas.
* Identified numerical and categorical features.
* Handled missing values.
* Prepared data for analysis and machine learning.



### 2. Exploratory Data Analysis (EDA)

Performed exploratory analysis to understand data distribution and relationships.

#### Visualizations

* Distribution of Influence Score
* Top 10 Influential Users
* Correlation Matrix Heatmap
* Followers vs Influence Score
* Outlier Detection using Boxplots

#### Key Findings

* Influence scores vary significantly across users.
* Followers show a strong relationship with influence score.
* Several features exhibit positive correlation with influence.



### 3. Graph Analytics

Graph-based metrics were analyzed to identify important users within the network.

#### Degree Centrality Analysis

Identified users with the highest number of direct network connections.

#### Betweenness Centrality Analysis

Identified users that act as bridges between different groups within the network.

#### Findings

* High degree centrality users tend to have higher influence scores.
* Users with high betweenness centrality play critical roles in information flow.



### 4. Machine Learning Models

The project implements two regression models to predict influence scores.

#### Linear Regression

Performance Metrics:

* MAE: 9.30
* MSE: 122.23
* R² Score: 0.027

Observation:

Linear Regression showed poor predictive performance and was unable to capture complex relationships within the dataset.


#### Random Forest Regression

Performance Metrics:

* MAE: 0.41
* MSE: 0.46
* R² Score: 0.996

Observation:

Random Forest significantly outperformed Linear Regression and achieved excellent predictive accuracy.



### 5. Feature Importance Analysis

Feature importance was extracted from the Random Forest model.

Top contributing features:

1. Followers
2. Degree Centrality
3. Betweenness Centrality
4. Engagement Rate

These results indicate that both audience size and network position strongly influence overall user influence.



## Results

### Best Model

Random Forest Regression

### Model Performance

| Metric   | Linear Regression | Random Forest |
| -------- | ----------------: | ------------: |
| MAE      |              9.30 |          0.41 |
| MSE      |            122.23 |          0.46 |
| R² Score |             0.027 |         0.996 |

### Key Insight

Followers, Degree Centrality, and Betweenness Centrality are the strongest predictors of influence score.



## Project Structure


Graph Analytics Project
│
├── Dataset
│   └── social_influence_dataset.xlsx
│
├── Notebook
│   └── Graph analysis on influencing datasets.ipynb
│
├── Results
│   ├── top10_influencers.png
│   └── other generated visualizations
│
├── Scripts
│   └── analysis.py
│
└── README.md

## Live Demo

Streamlit Dashboard:
[https://graph-analytics-social-influence-c8ureuaa9krff55vcr6adh.streamlit.app/](https://graph-analytics-social-influence-c8ureuaa9krff55vcr6adh.streamlit.app/)

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- GitHub



## Conclusion

This project demonstrates the application of graph analytics and machine learning for social influence analysis. Network centrality measures combined with user engagement metrics provide valuable insights into influence patterns. Random Forest Regression proved highly effective for influence score prediction and achieved near-perfect predictive performance on the dataset.



## Author

Bharath Kalyan S
Data Analytics Enthusiast | UI UX Designer 














