# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body='Some body', to='584241700615'):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC12033766183f3c86a9b5ea253004e7c0'
    auth_token = 'c7ace38f4e9a4fd066d22e3c43c7ad14'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+13346058062',
                        to='+'+to
                    )

    print(message.sid)