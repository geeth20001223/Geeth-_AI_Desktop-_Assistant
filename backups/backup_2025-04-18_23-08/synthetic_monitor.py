import requests
import time
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender_email = "shamal.geethanjanpathirana@gmail.com"
    sender_password = "zozg rvmx zuio tpof"
    receiver_email = "shamal.geethanjanpathirana@gmail.com"

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email failed to send: {e}")

def synthetic_test_api_status():
    start_time = time.time()
    try:
        response = requests.get('http://localhost:8000/api/status')
        end_time = time.time()
        return {
            'response_time': end_time - start_time,
            'status_code': response.status_code,
            'is_successful': response.status_code == 200
        }
    except Exception as e:
        return {'response_time': 0, 'status_code': 0, 'is_successful': False, 'error': str(e)}

def synthetic_test_another_endpoint():
    start_time = time.time()
    try:
        response = requests.get('http://localhost:8000/another_endpoint')
        end_time = time.time()
        return {
            'response_time': end_time - start_time,
            'status_code': response.status_code,
            'is_successful': response.status_code == 200
        }
    except Exception as e:
        return {'response_time': 0, 'status_code': 0, 'is_successful': False, 'error': str(e)}

if __name__ == "__main__":
    result_api_status = synthetic_test_api_status()
    print("API Status:", result_api_status)

    if not result_api_status['is_successful']:
        send_email("Synthetic Monitoring Failure - API Status", str(result_api_status))

    result_another = synthetic_test_another_endpoint()
    print("Another Endpoint:", result_another)

    if not result_another['is_successful']:
        send_email("Synthetic Monitoring Failure - Another Endpoint", str(result_another))
