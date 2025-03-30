# MentalHealthLog

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

## Features

- 📝 Daily mental health logging
- 🌓 Dark/Light theme toggle
- 📊 Emotion and feeling level tracking
- 📅 Custom date/time entry support
- 📧 Automated email reports
- 📱 Responsive design for mobile and desktop
- 🔒 Privacy-focused (data sent via email, not stored)

## Technologies Used

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

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd mental-health-tracker
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

4. Create a `.env` file in the root directory with the following variables:
```plaintext
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-specific-password
RECEIVER_EMAIL=destination@email.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:3000
```

## Usage

1. Fill out the mental health questionnaire:
   - Select current date/time or customize
   - Rate your feeling level
   - Choose your current emotion
   - Add contributing factors
   - Note your thoughts and needs
   - Log smoking and drinking status

2. Submit the form to:
   - Generate a CSV report
   - Send an email with the data
   - Receive confirmation of submission

## Project Structure

```
mental-health-tracker/
│
├── app.py                 # Flask backend application
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
│
├── static/
│   ├── index.html        # Frontend application
│   └── styles.css        # (Optional) Separated styles
│
└── README.md             # This file
```

## Security Considerations

- Environment variables used for sensitive data
- No data stored on server
- Direct email transmission of data
- Input sanitization
- CORS protection

## Future Improvements

- Add user authentication
- Implement data visualization
- Add database storage option
- Include export functionality
- Add historical data viewing
- Implement progress tracking
- Add custom emotion/factor tags
- Include crisis resources
- Add coping strategy suggestions

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Mental health resources and crisis hotlines
- Flask documentation
- MDN Web Docs
- Your contributions and feedback




