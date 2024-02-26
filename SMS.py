import vonage

def send(message):
    api_key = 'API' # Replace with your API key
    api_secret = 'API' # Replace with your API secret
    # Sender and recipient phone numbers
    sender = 'PHONE' # Your Vonage number
    recipient = 'PHONE'  # Should be in international format without leading '+'

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
