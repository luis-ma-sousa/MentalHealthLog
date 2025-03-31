# 📝 MentalHealthLog Web Application

A full-stack web application for tracking mental health metrics and emotions. The application allows users to log their emotional state, contributing factors, and habits, sending the data via email in CSV format for record-keeping.

Created with ❤️ for better mental health tracking.

## 🌐 Hosting & Access

This app is live and accessible via **Glitch**:  
🔗 [https://mentalhealthlog.glitch.me/](https://mentalhealthlog.glitch.me/)

You can try out the form directly in your browser — no installation required.

---

## 🔒 Mocked Environment

⚠️ **Note:** This repository includes a mocked version of `app.py` and a `.env.example` file.  
Sensitive credentials and production email settings have been replaced with placeholder values for public sharing and demonstration purposes.

To run locally, rename `.env.example` to `.env` and add your own email credentials.

---

## ✨ Features

- 📝 Daily mental health logging
- 🌓 Dark/Light theme toggle
- 📊 Emotion and feeling level tracking
- 📅 Custom date/time entry support
- 📧 Automated email reports
- 📱 Responsive design for mobile and desktop
- 🔒 Privacy-focused (data sent via email, not stored)

## 🛠️ Technologies Used

### Backend
- Python 3.x
- Flask (Web Framework)
- Flask-CORS
- SMTP (Email functionality)

### Frontend
- HTML5
- CSS3 (Modern styling with CSS Variables)
- JavaScript (ES6+)
- Responsive Design

### Data Management
- CSV Generation
- JSON for API communication
- Environment Variables for Configuration

## 📋 Installation

1. Clone the repository:
```bash
git clone https://github.com/luis-ma-sousa/MentalHealthLog.git
cd MentalHealthLog/App
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask flask-cors python-dotenv
```

4. Create a `.env` file in the App directory with the following variables:
```plaintext
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-specific-password
RECEIVER_EMAIL=destination@email.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## 🚀 Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:3000
```

## 📱 Usage

1. Fill out the mental health questionnaire:
   - Select current date/time or customize
   - Rate your feeling level
   - Choose your current emotion
   - Add contributing factors
   - Note your thoughts and needs
   - Log exercise and meditation status

2. Submit the form to:
   - Generate a CSV report
   - Send an email with the data
   - Receive confirmation of submission

## 📁 Project Structure

```
App/
│
├── app.py                 # Flask backend application
├── app_mocked.py          # Mocked version for GitHub sharing
├── .env                   # Environment variables (not included)
├── .env.example           # Example environment file
├── requirements.txt       # Python dependencies
│
├── static/
│   ├── index.html         # Frontend application
│   ├── styles.css         # CSS styles
│   └── scripts.js         # Frontend JavaScript
│
└── README.md              # This file
```

## 🔐 Security Considerations

- Environment variables used for sensitive data
- No data stored on server
- Direct email transmission of data
- Input sanitization
- CORS protection

## 🔄 Integration with Dashboard

This app sends data via email, which is then processed by the [Analysis Dashboard](../Notebook/README.md) component. For information on how to set up the complete system, refer to the [main project README](../README.md).

## 🚧 Future Improvements

- Add user authentication
- Implement export functionality
- Add custom emotion/factor tags
- Include crisis resources
- Add coping strategy suggestions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is available for personal use.

## 📚 Acknowledgments

- Mental health resources and crisis hotlines
- Flask documentation
- MDN Web Docs
