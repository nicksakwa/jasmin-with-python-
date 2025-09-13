import requests

# Jasmin SMS Gateway API endpoint
JASMIN_API_URL = "http://your_jasmin_server_ip:1401/send"

# Your Jasmin API credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# SMS details
SENDER_ID = "YourSender"  # The sender ID (e.g., a short code or name)
RECIPIENT = "256771234567"  # The recipient's phone number
MESSAGE_CONTENT = "Hello, this is a test SMS from my app!"

# Construct the payload
payload = {
    "username": USERNAME,
    "password": PASSWORD,
    "to": RECIPIENT,
    "from": SENDER_ID,
    "content": MESSAGE_CONTENT
}

# Send the HTTP POST request
try:
    response = requests.post(JASMIN_API_URL, data=payload)
    
    # Check the response status
    if response.status_code == 200:
        print("SMS sent successfully!")
        print("Response from Jasmin:", response.text)
    else:
        print(f"Failed to send SMS. Status code: {response.status_code}")
        print("Response from Jasmin:", response.text)
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")