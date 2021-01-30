import os 
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


messages = client.messages.list(limit=20)

for message in messages:
    print(message.body)