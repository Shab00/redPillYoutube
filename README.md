## Project Description

### Background
The term "red pill" originates from the 1999 film *The Matrix*, where taking the red pill symbolizes awakening to harsh truths about reality. In contemporary culture, especially online, "red pill" has been adopted by various communities to describe content that challenges mainstream narratives, often focusing on topics like masculinity, self-improvement, anti-feminism, conspiracy theories, political incorrectness, and critiques of societal norms.

This project aims to analyze "red pill" content on YouTube by collecting and analyzing data from selected channels. By examining video metadata and comments, we seek to uncover trends, sentiments, and engagement patterns within this niche community.

---

### Objectives
1. **Data Collection:**
   - Retrieve video metadata (e.g., titles, views, likes, upload dates) from selected "red pill" YouTube channels.
   - Collect comments from videos to analyze audience engagement and sentiment.

2. **Data Analysis:**
   - Perform exploratory data analysis (EDA) to identify trends in video performance and audience engagement.
   - Conduct sentiment analysis on comments to understand the tone and themes of audience discussions.
   - Visualize findings to communicate insights effectively.

3. **Insights:**
   - Identify common themes and topics in "red pill" content.
   - Analyze how audience engagement varies across different types of content.
   - Provide actionable insights for researchers, content creators, and policymakers.

---

### Methodology
1. **Data Retrieval:**
   - Use the YouTube Data API to collect video metadata and comments.
   - Handle pagination and quota limits to ensure comprehensive data collection.

2. **Data Cleaning:**
   - Clean and preprocess raw data (e.g., remove duplicates, handle missing values).
   - Structure data for analysis (e.g., combine metadata and comments into a single dataset).

3. **Data Analysis:**
   - Perform EDA to uncover trends in video performance (e.g., views, likes, comments).
   - Use natural language processing (NLP) techniques for sentiment analysis on comments.
   - Generate visualizations (e.g., bar charts, word clouds, time series plots) to communicate findings.

4. **Insights and Reporting:**
   - Summarize key findings and insights.
   - Provide recommendations for further research or action.

---

### Significance
This project provides a data-driven approach to understanding "red pill" content on YouTube. By analyzing video metadata and comments, we can:
- Identify the most popular topics and themes within the "red pill" community.
- Understand how audiences engage with this type of content.
- Provide insights for researchers studying online communities and digital culture.
- Inform content creators and policymakers about the impact of "red pill" content.

---

### Future Work
- Expand the dataset to include more channels and videos.
- Perform advanced NLP analysis (e.g., topic modeling, emotion detection).
- Compare "red pill" content with other types of YouTube content (e.g., mainstream, educational).
- Develop a dashboard for real-time monitoring of "red pill" content trends.

---

## Notebooks

### 1. Video Metadata Retrieval and Analytics
- **File:** `1_video_metadata_retrieval_analytics.ipynb`
- **Purpose:** Retrieves video metadata (e.g., titles, views, likes, upload dates) from selected YouTube channels.
- **Output:** Raw metadata stored in `data/raw/video_metadata.csv`.

### 2. YouTube Comment Data Collection
- **File:** `2_youtube_comment_data_collection.ipynb`
- **Purpose:** Retrieves comments from videos using the YouTube Data API. Handles pagination, quota limits, and errors.
- **Output:** Raw comments stored in `data/raw/comments/` (one file per video).

### 3. Data Cleaning and Preprocessing
- **File:** `3.cleaningData.ipynb`
- **Purpose:** Cleans and preprocesses raw video metadata and comments. Handles missing values, duplicates, and invalid entries. Applies log transformations to skewed data (e.g., views, likes, comment counts).
- **Output:** Cleaned data stored in `data/processed/cleaned_video_metadata.csv` and `data/processed/cleaned_comments.csv`.

### 4. Red Pill Content Analysis and Insights
- **File:** `3_red_pill_content_analysis_insights.ipynb`
- **Purpose:** Analyzes the collected data to uncover trends, sentiments, and engagement patterns.
- **Output:** Visualizations, insights, and processed data stored in `data/processed/`.

### 5. Comment Section Deep Dive & Final Analysis 
- **File:** `5.commentsSecton.ipynb`
- **Purpose:** Integrates advanced NLP analyses including sentiment analysis, emotion detection, aspect-based sentiment, and key phrase extraction. Combines and visualizes findings for actionable insights and final reporting.
- **Output:** Comprehensive visualizations, multi-dimensional and insights.

---

## Data Folder
- **`data/raw/`:** Contains raw data downloaded from YouTube (e.g., video metadata, comments).
- **`data/processed/`:** Contains cleaned and processed data ready for analysis.

## Models Folder
- **`models/bert/`:** Stores BERT-based model files (e.g., `my_bert_model.zip`).
- **`models/dtm/`:** Contains topic modeling artifacts such as Dynamic Topic Model (`dtm.joblib`).
- **`models/lda/`:** Includes Latent Dirichlet Allocation model files (`lda_model.joblib`).

---

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Google Cloud Platform (GCP) account with YouTube Data API enabled
- API key for YouTube Data API
