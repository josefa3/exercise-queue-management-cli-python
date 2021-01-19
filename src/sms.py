# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os

def send(body='Some body', to=''):
    account_sid = os.environ["ACCOUNT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+18587269832',
                        to='+'+to
                    )

    print(message.sid)