# 🧠 MentalHealthLog Project

This project consists of two complementary components:

## 📝 Data Collection Web App
Location: `/app` directory
- Flask web application for daily logging of mental health data
- Sends data via email in CSV format
- User-friendly interface with responsive design
- [View App README](MentalHealthLog/App/README.md)

## 📊 Data Analysis Dashboard
Location: `/notebook` directory
- Jupyter notebook for analyzing collected mental health data
- Visualizations of emotional patterns and activity correlations
- Insights on mood patterns, activity impacts, and contributing factors
- [View Dashboard README](MentalHealthLog/Notebook/README.md)

## 🔄 How They Work Together

1. Users log their mental health data through the web application
2. Data is emailed as CSV attachments
3. The dashboard notebook fetches these emails and processes attached CSV files
4. Visualizations and insights are generated to help identify patterns over time

## 🛠️ Getting Started

For setup instructions, see the individual README files in each component's directory:
- [Web App Setup](./app/README.md#installation)
- [Dashboard Setup](./dashboard/README.md#setup-and-usage)

Created with ❤️ for better mental health tracking by Luís Sousa.
