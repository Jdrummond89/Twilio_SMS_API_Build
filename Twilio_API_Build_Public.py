# Download the helper library from https://www.twilio.com/docs/python/install
# pip3 install twilio
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Get your auth token and account sid by creating an account with Twilio 
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = os.environ["TWILIO_AUTH_TOKEN"] 
client = Client(account_sid, auth_token)

# These are sample numbers, make sure to change to your own
message = client.messages.create(
  body="Ahoy! -Jdrummond",
  from_="+134624549638",
  to="+12035518954"
)

print(message.sid)