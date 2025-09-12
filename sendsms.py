import requests

JASMIN_API_URL = "http://yourjasmin_server_ip:1401/send"

USERNAME = "your_username"
PASSWORD = "your_password"

SENDER = "your_sender_id"
RECIPIENT = "recipient_phone_number"
MESSAGE_CONTENT = "Hello world this is Jasmin SMS Gateway"

payload = {
    "username": USERNAME,
    "password": PASSWORD,
    "from": SENDER,
    "to": RECIPIENT,
    "content": MESSAGE_CONTENT
}

try:
    response = responses.post(JASMIN_API_URL, data=payload)

    if response.status_code == 200:
        print("message sent successfully")
        print("Response from jasmin:", response.text)
    else:
        print("Failed to send SMS. Status code:", {response.status_code}")
        print(" Response from jasmin:" , response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")