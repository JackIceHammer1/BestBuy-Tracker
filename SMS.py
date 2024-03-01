import vonage

def send(message):
    api_key = 'API' # Replace with your Vonage API key
    api_secret = 'API' # Replace with your Vonage API secret
    sender = 'PHONE' # Your Vonage phone number
    recipient = 'PHONE'  # Recipient phone number, international format without leading '+'

    # Create a Vonage client
    client = vonage.Client(key=api_key, secret=api_secret)
    sms = vonage.Sms(client)

    # Send SMS message
    response = sms.send_message({
        'from': sender,
        'to': recipient,
        'text': "In Stock"
    })

    if response['messages'][0]['status'] == '0':
        print('Message sent successfully!')
    else:
        print(f'Error: {response["messages"][0]["error-text"]}')
