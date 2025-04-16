import requests
import time
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your password or app password
    receiver_email = "recipient_email@example.com"  # Replace with recipient email

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Email failed to send: {e}")

def synthetic_test_api_status():
    start_time = time.time()
    response = requests.get('http://localhost:8000/api/status')  # API Status
    end_time = time.time()
    response_time = end_time - start_time
    status_code = response.status_code
    return {
        'response_time': response_time,
        'status_code': status_code,
        'is_successful': status_code == 200
    }

def synthetic_test_another_endpoint():
    start_time = time.time()
    response = requests.get('http://localhost:8000/another_endpoint')  # Another Endpoint
    end_time = time.time()
    response_time = end_time - start_time
    status_code = response.status_code
    return {
        'response_time': response_time,
        'status_code': status_code,
        'is_successful': status_code == 200
    }

if __name__ == "__main__":
    result_api_status = synthetic_test_api_status()
    print(f"API Status - Response Time: {result_api_status['response_time']:.2f} seconds")
    print(f"API Status - Status Code: {result_api_status['status_code']}")
    print(f"API Status - Test Passed: {result_api_status['is_successful']}")

    if not result_api_status['is_successful']:
        message_body = f"API Status test failed at {time.ctime()}: {result_api_status}"
        send_email("Synthetic Monitoring Failure - API Status", message_body)

    result_another_endpoint = synthetic_test_another_endpoint()
    print(f"Another Endpoint - Response Time: {result_another_endpoint['response_time']:.2f} seconds")
    print(f"Another Endpoint - Status Code: {result_another_endpoint['status_code']}")
    print(f"Another Endpoint - Test Passed: {result_another_endpoint['is_successful']}")

    if not result_another_endpoint['is_successful']:
        message_body = f"Another Endpoint test failed at {time.ctime()}: {result_another_endpoint}"
        send_email("Synthetic Monitoring Failure - Another Endpoint", message_body)
