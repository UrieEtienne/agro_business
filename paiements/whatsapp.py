from twilio.rest import Client


def send_whatsapp_message(numero, message):

    account_sid = 'TWILIO_SID'

    auth_token = 'TWILIO_TOKEN'

    client = Client(
        account_sid,
        auth_token
    )

    client.messages.create(

        from_='whatsapp:+14155238886',

        body=message,

        to=f'whatsapp:{numero}'

    )