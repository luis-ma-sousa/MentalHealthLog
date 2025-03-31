# 🧠 Mental Health Log Dashboard

A comprehensive tool for tracking, analyzing, and visualizing emotional well-being and activity patterns over time.

## 📊 Overview

This Mental Health Log Dashboard is a data analysis and visualization tool designed to help track emotional states, physical activities, and their correlations over time. The dashboard processes data collected through regular emotional logs and provides insightful visualizations and statistical analysis to help identify patterns and trends in mental well-being.

## ✨ Features

### 📥 Data Collection & Processing
- **📧 Email Integration**: Automatically retrieves log entries from emails with "Mental Health Log" in the subject line
- **🔄 Data Compilation**: Combines multiple CSV files into a standardized format for analysis
- **🕒 DateTime Normalization**: Ensures consistent date and time formatting across all entries

### 📈 Visualizations
- **😊 Emotion Distribution**: Pie chart showing the frequency of different emotional states
- **🌡️ Feeling Intensity**: Distribution of feelings from "Very Unpleasant" to "Very Pleasant"
- **⏰ Time-of-Day Mood Patterns**: Heatmap showing how mood varies throughout the day
- **🔄 Emotion-Activity Relationships**: Sankey diagram visualizing connections between emotions and activities (Exercise, Meditation)
- **🌱 Contributing Factors Analysis**: Sunburst chart identifying common triggers or contributing factors
- **🌓 Day vs. Night Mood Patterns**: Comparison of emotional states and activities between daytime and nighttime periods
- **🏃‍♂️ Exercise Pattern Analysis**: Detailed breakdown of exercise probability by emotional state, time of day, and contributing factors

### 🔍 Insights & Analytics
- **📊 Mood Volatility**: Quantifies daily mood fluctuations
- **🤝 Activity Correlations**: Analyzes the relationship between activities (Exercise, Meditation) and emotional well-being
- **⏱️ Peak Hours**: Identifies best and worst hours for mood
- **📋 Emotion-Feeling Combinations**: Cross-tabulation of emotions and feeling intensities
- **💪 Emotional Response to Activities**: Compares feeling intensity when engaging in vs. not engaging in specific activities

## 🚀 Setup and Usage

### 📋 Prerequisites
- Python 3.8+
- Required libraries: pandas, plotly, numpy, imaplib (for email functionality)

### 💻 Installation
1. Clone this repository
2. Install required packages:
   ```
   pip install pandas plotly numpy openpyxl
   ```

### ⚙️ Configuration
For email functionality, update the credentials in the email retrieval section of the notebook:
```python
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
IMAP_SERVER = "imap.example.com"
```

For security, it's recommended to use environment variables or a secure configuration file rather than hardcoding credentials.

### 📄 Data Structure
The dashboard expects CSV files with at least the following columns:
- `DateTime`: The date and time of the log entry
- `Feeling`: The intensity of the feeling (Very Unpleasant, Unpleasant, Slightly Unpleasant, Neutral, Pleasant, Very Pleasant)
- `Emotion`: The specific emotion experienced (Joy, Love, Calm, Hope, Contentment, Surprise, Nostalgia, Sadness, Anger, Fear, Drained, Anxiety, Frustration)
- `Exercise`: Whether exercise was performed (yes/no)
- `Meditation`: Whether meditation was practiced (yes/no)
- `Contributing Factors`: Comma-separated list of factors that influenced the emotional state
- `Thoughts`: Additional notes or thoughts about the entry

### 🏃‍♂️ Running the Dashboard
1. Execute the notebook cells sequentially
2. If using email retrieval, the system will fetch new entries automatically
3. Otherwise, place your CSV files in the designated folder
4. The notebook will generate all visualizations and insights

## 🔎 Interpreting Results

### 💪 Activity Impact
The dashboard helps identify how activities like exercise and meditation correlate with emotional states. Look for:
- Differences in mood scores between days with and without certain activities
- Emotional states more likely to lead to exercise or meditation
- Time periods when activities have the greatest positive impact

### 😊 Emotional Patterns
Identify recurring patterns in your emotional wellbeing:
- Times of day when you typically feel best/worst
- Contributing factors most associated with positive or negative emotions
- Day vs. night emotional differences

## 🔒 Data Privacy & Security

This dashboard processes personal health information. Consider these security measures:
- Never share notebooks with credentials
- Store raw data files securely
- Consider encrypting sensitive data

## 👤 Author

**Luís Sousa**  
Contact: luis.95.sousa.31@gmail.com

## 📜 License

This project is for personal use.
