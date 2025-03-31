# 🧠 MentalHealthLog Project

## 🌐 **[Try The App Now:  https://mentalhealthlog.glitch.me/](https://mentalhealthlog.glitch.me/)**

A full-stack solution for tracking, analyzing, and visualizing mental health data to identify patterns and improve well-being.

## 🌟 Project Overview

MentalHealthLog consists of two complementary components that work together to provide a complete mental health tracking solution:

1. **Data Collection Web App**: A responsive Flask web application for daily logging of mental health metrics
2. **Data Analysis Dashboard**: A Jupyter notebook for processing and visualizing the collected data

## 📝 Data Collection Web App

Location: `/App` directory

- Flask-based web application for daily mental health logging
- Dark/Light theme toggle for comfortable use at any time
- Tracks emotions, feeling levels, contributing factors, and activities
- Sends data via email in CSV format for privacy
- Mobile-responsive design for logging on any device

**[View App Details](./App/README.md)**

## 📊 Data Analysis Dashboard

Location: `/Notebook` directory

- Jupyter notebook for analyzing collected mental health data
- Comprehensive visualizations of emotional patterns and activity correlations
- Time-based analysis showing patterns by hour, day vs night
- Activity impact analysis for exercise and meditation
- Contributing factors analysis to identify emotional triggers

**[View Dashboard Details](./Notebook/README.md)**

## 📈 Sample Visualizations

Want to see what insights you can gain? Check out the **[results gallery](./Mock_results_gallery.md)** for sample visualizations from the dashboard:

- Emotion distributions and mood timelines
- Exercise and meditation impact analysis
- Day vs. night emotional pattern comparisons
- Contributing factors breakdown

## 🔄 How It Works

1. **Log Data**: Users record their emotional state, activities, and contributing factors through the web application
2. **Email Delivery**: Data is sent via email as CSV attachments (not stored on any server)
3. **Process Data**: The dashboard notebook fetches these emails and processes the attached CSV files
4. **Analyze Patterns**: Visualizations and insights are generated to help identify patterns over time

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask (for web app)
- Jupyter Notebook (for dashboard)
- Required Python packages (see requirements.txt in each component)

### Setup Instructions
For detailed setup instructions, see the individual README files:
- **[Web App Setup](./App/README.md#installation)**
- **[Dashboard Setup](./Notebook/README.md#setup-and-usage)**

## 🔒 Privacy & Security

- Data is sent directly via email rather than stored on a server
- Mock data is provided for testing without using personal information
- Example credentials and configuration files are provided with placeholders

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is available for personal use.

---

Created with ❤️ for better mental health tracking by [Luís Sousa](https://github.com/luis-ma-sousa).
