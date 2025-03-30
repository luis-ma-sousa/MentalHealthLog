from flask import Flask, request, jsonify, Response
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import io
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__, static_folder="static")
CORS(app)

# Email Configuration (loaded from .env)
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your_email@example.com")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "your_password")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "receiver_email@example.com")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Default: 587 for TLS

@app.route("/___glitch_loading_status___")
def loading_status():
    return Response(status=200)

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/save-log", methods=["POST"])
def save_log():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        # Updated required fields to match the React component
        required_fields = [
            'datetime',  # New field for custom/current datetime
            'feeling',
            'emotion',
            'factors',
            'thoughts',
            'needs',
            'smoked',
            'drank'
        ]
        
        if not all(field in data for field in required_fields):
            missing_fields = [field for field in required_fields if field not in data]
            return jsonify({
                "error": "Missing required fields",
                "missing_fields": missing_fields
            }), 400
            
        # Process datetime
        try:
            log_datetime = datetime.fromisoformat(data['datetime'].replace('Z', '+00:00'))
            formatted_datetime = log_datetime.strftime('%d/%m/%Y %H:%M:%S')
        except (ValueError, AttributeError):
            formatted_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            
        # Sanitize and prepare data for CSV
        sanitized_data = {
            'DateTime': formatted_datetime,
            'Feeling': str(data.get('feeling', '')),  # This will now be the text label
            'Emotion': str(data.get('emotion', '')),
            'Contributing Factors': str(data.get('factors', '')),
            'Thoughts': str(data.get('thoughts', '')),
            'Needs': str(data.get('needs', '')),
            'Smoked': str(data.get('smoked', '')),
            'Drank': str(data.get('drank', ''))
        }
        
        # Create CSV
        csv_output = io.StringIO()
        writer = csv.writer(csv_output)
        
        # Write headers and data
        writer.writerow(sanitized_data.keys())
        writer.writerow(sanitized_data.values())
        
        csv_output.seek(0)
        
        # Prepare email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f"Mental Health Log - {formatted_datetime}"
        
        # Create email body with a summary
        email_body = f"""
New mental health log entry:

Date and Time: {formatted_datetime}
Feeling: {data.get('feeling')}
Emotion: {data.get('emotion')}
Contributing Factors: {data.get('factors')}

Full details are in the attached CSV file.
        """
        
        msg.attach(MIMEText(email_body, 'plain'))
        
        # Attach CSV
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(csv_output.getvalue())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition', 
            f'attachment; filename="mental_health_log_{formatted_datetime}.csv"'
        )
        msg.attach(part)
        
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            
        return jsonify({
            "message": "Log saved successfully",
            "timestamp": formatted_datetime
        }), 201
        
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)